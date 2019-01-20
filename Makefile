all: go

go:
	protoc -I ./proto --go_out=plugins=grpc:${GOPATH}/src ./proto/opensnitch/network/*.proto
	protoc -I ./proto --go_out=plugins=grpc:${GOPATH}/src ./proto/opensnitch/rules/*.proto
	protoc -I ./proto --go_out=plugins=grpc:. ./proto/opensnitch/ui/*.proto
	cp -r ./opensnitch/ui ./
	rm -r ./opensnitch/ui
	# Different for ui because Linux grpc plugin outputs it in the wrong directory