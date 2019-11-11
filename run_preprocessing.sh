# move this to berkeley directory

for dir in `find /iesl/canvas/nnayak/logic-factuality/final_chunks/ -type d | grep text | sort`
do
	preprocessed_dir="${dir/text/preprocessed}" 
	java -Xmx50g -cp ./berkeley-entity-1.0.jar \
		edu.berkeley.nlp.entity.preprocess.PreprocessingDriver \
		++base.conf -execDir exec_dir -inputDir $dir \
		-outputDir $preprocessed_dir
done
