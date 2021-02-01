runserver:
	PYTHONPATH=/home/kees/protoTrees/generated python tree_server.py

compile_protobuffers:
	python -m grpc.tools.protoc -I definitions --python_out=generated --experimental_allow_proto3_optional --grpc_python_out=generated definitions/tree.proto

run_example:
	node ./treeClient.js 10
