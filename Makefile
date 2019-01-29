all: go py3

go:
	protoc -I ./proto --go_out=plugins=grpc:. ./proto/opensnitch/network/*.proto
	protoc -I ./proto --go_out=plugins=grpc:. ./proto/opensnitch/rules/*.proto
	protoc -I ./proto --go_out=plugins=grpc:. ./proto/opensnitch/ui/*.proto
	cp -r github.com/Northern-Lights/os-rules-engine/* .
	rm -rf github.com/
	cp -r ./opensnitch/ui ./
	rm -r ./opensnitch/ui
	# Different for ui because Linux grpc plugin outputs it in the wrong directory

py3:
	python3 -m grpc_tools.protoc -I ./proto \
		--python_out=./python3/ \
		./proto/opensnitch/network/*.proto
	python3 -m grpc_tools.protoc -I ./proto \
		--python_out=./python3/ \
		./proto/opensnitch/rules/*.proto
	python3 -m grpc_tools.protoc -I ./proto \
		--python_out=./python3/ \
		--grpc_python_out=./python3/ \
		./proto/opensnitch/ui/*.proto
	find ./python3/opensnitch -type d -exec touch {}/__init__.py \;