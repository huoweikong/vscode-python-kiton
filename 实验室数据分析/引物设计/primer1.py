#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   primer1.py
@Time         :   2020/07/05 02:21:26
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
library(tcltk)
library(Biostrings)
#* 读取FASTA格式序列
seqs.fasta.file <- tk_choose.files(default = "~//", multi = FALSE, caption = "Sequence file")
seqs <- readDNAStringSet(seqs.fasta.file)
seqs.path <- dirname(seqs.fasta.file)
#* 设置Primer3参数文件 p3_settings_file
p3.paras <- list(
  PRIMER_TASK="generic",
  PRIMER_NUM_RETURN=1000,
  PRIMER_DNA_CONC=500,
  PRIMER_DNTP_CONC=0.8,
  PRIMER_SALT_CORRECTIONS=1,
  PRIMER_SALT_MONOVALENT=50,
  PRIMER_SALT_DIVALENT=1.5,
  PRIMER_MAX_END_GC=2,
  PRIMER_MIN_GC=35,
  PRIMER_MAX_GC=65,
  PRIMER_MIN_TM=58,
  PRIMER_MAX_TM=64,
  PRIMER_OPT_TM=60,
  PRIMER_MIN_SIZE=18,
  PRIMER_MAX_SIZE=26,
  PRIMER_OPT_SIZE=20,
  PRIMER_PAIR_MAX_DIFF_TM=2,
  PRIMER_PRODUCT_SIZE_RANGE="70-120",
  PRIMER_PICK_ANYWAY=1
  )
p3.paras <- paste(names(p3.paras), '=', p3.paras, sep='')
p3.paras <- c(
  "Primer3 File - http://primer3.sourceforge.net",
  "P3_FILE_TYPE=settings",
  p3.paras,
  "="
  )
p3.settings.file <- file.path(seqs.path, "p3.settings.file")
writeLines(p3.paras, p3.settings.file)
tmpfiles <- p3.settings.file
#* 设置Primer3参数文件 input_file
seq.ids <- paste("SEQUENCE_ID=", names(seqs), sep='')
seq.templates <- paste("SEQUENCE_TEMPLATE=", as.character(seqs), sep='')
content.input.file <- paste(seq.ids, seq.templates, '=', sep="\n")
input.file <- file.path(seqs.path, "p3.input.file")
writeLines(content.input.file, input.file)
tmpfiles <- c(tmpfiles, input.file)
#* 运行 Primer3 获取引物
output.file <- file.path(seqs.path, "p3.temp1")
p3.settings <- paste("-p3_settings_file=", p3.settings.file, sep='')
p3.output <- paste("-output=", output.file, sep='')
cmd <- paste("primer3_core", p3.settings, p3.output, input.file)
system(cmd)
tmpfiles <- c(tmpfiles, output.file)
#* 解析 Primer3 输出文件
#  下面只保留了引物名称、序列和TM值，需要更多参数请自己设置
p3.results <- readLines(output.file)
group.start <- grep("SEQUENCE_ID", p3.results)
group.end <- c(group.start[-1]-1, length(p3.results))
seq.ids <- names(seqs)
for(i in 1:length(seq.ids)){
  sel <- group.start[i]:group.end[i]
  p3.results[sel] <- paste(seq.ids[i], p3.results[sel], sep="_")
}
writeLines(p3.results, output.file)
primers.seq <- p3.results[grep("(LEFT|RIGHT)_[0-9]+_SEQUENCE=", p3.results)]
primers.name <- gsub("(.+)_PRIMER(_[^=]+)_SEQUENCE.*", "\\1\\2", primers.seq)
primers.name <- gsub("LEFT", "L", primers.name)
primers.name <- gsub("RIGHT", "R", primers.name)
primers.seq <- gsub(".+=(.+)", "\\1", primers.seq)
primers.tm <- p3.results[grep("(LEFT|RIGHT)_[0-9]+_TM=", p3.results)]
primers.tm <- gsub(".+=(.+)", "\\1", primers.tm)
primers <- data.frame(name=primers.name, seq=primers.seq, TM=primers.tm)
#* BLAST 分析，输出便于程序解析的 m8 格式
blast.in <- file.path(seqs.path, "blast.in")
xxx <- paste(">", primers.name, sep='')
xxx <- paste(xxx, primers.seq, sep="\n")
writeLines(xxx, blast.in)
rm(xxx)
tmpfiles <- c(tmpfiles, blast.in)
blast.db <- tk_choose.files(default = "~//", multi = FALSE, caption = "BLAST database")
blast.db <- sub("(.+)\\.[^\\.]+", "\\1", blast.db)
blast.out <- file.path(seqs.path, "blast.out")
cmd <- paste("blastall -p blastn -e 10000 -F F -m 8 -a 4 -i",
             blast.in, "-o", blast.out, "-d", blast.db)
system(cmd)
tmpfiles <- c(tmpfiles, blast.out)
#* 解析 BALST 输出结果。 m8 结果共有12列，分别为：
# 1. Query id
# 2. Subject id
# 3. % identity
# 4. alignment length
# 5. mismatches
# 6. gap openings
# 7. q.start
# 8. q.end
# 9. s.start
# 10. s.end
# 11. e-value
# 12. bit score
# 这里我们仅要求 q.start=1, q.end=引物长度 的比对结果有且仅有一个，即目标序列的匹配
blast.result <- read.table(blast.out, stringsAsFactors = FALSE)[,c(1,7,8)]
sel <- blast.result[,2]==1
blast.result <- blast.result[sel,]
primers.n <- length(primers.name)
sel <- rep(FALSE, primers.n)
for(i in 1:primers.n){
  sel.sub <- blast.result[,1]==primers.name[i]
  blast.sub <- blast.result[sel.sub,3]
  max.qend <- max(blast.sub)
  blast.sub <- blast.sub[blast.sub==max.qend]
  if(length(blast.sub)==1 & max.qend==nchar(primers.seq[i]))
    sel[i] <- TRUE
}
primers <- primers[sel,]
#* 删除临时文件，输出结果
file.remove(tmpfiles)
result.file <- file.path(seqs.path, "primer3.results.csv")
write.csv(primers, result.file, quote=FALSE, row.names=FALSE)
