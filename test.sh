#!/bin/bash

DRE="118105807"
IN_FILE="exemplo.txt"
OUT_FILE="aluno.txt"
ANSWER_FILE="saida.txt"
DRE_FILE=${DRE}.py

FILE_LIST="${DRE_FILE} ${IN_FILE} ${ANSWER_FILE}"

# find all files that are not stating with "." of type d (directory) and
# sort them as version numbers
DIRLIST_ALL=`find . ! -path '*/\.*' -type d | sort -V`
DIRLIST=${DIRLIST_ALL:1}

for D in ${DIRLIST}
do
	pushd . 2>&1 >/dev/null
	cd ${D}

	#dos2unix
	find *.txt -maxdepth 1 -type f -exec perl -i -pe 'tr/\r//d' {} \;
	
	BASE=$(basename ${D})

	getout=false
	for file in $FILE_LIST; do
		if [ ! -f ${file} ]; then
			echo "Test case ${BASE} [${file} NOT FOUND]"
			popd 2>&1 >/dev/null
			getout=true
			break
		fi
	done

	if $getout; then continue;
	fi
	
	python2 ${DRE_FILE} < ${IN_FILE} > ${OUT_FILE}

	diff ${OUT_FILE} ${ANSWER_FILE}
	
	if [ $? -ne 0 ]; then
		echo "Test case ${BASE} [WRONG]"
	else
		echo "Test case ${BASE} [OK]"
	fi
	
	rm ${OUT_FILE}
	
	popd 2>&1 >/dev/null
done
