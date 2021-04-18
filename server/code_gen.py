"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc_tools import protoc
import os

SERVER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'server_stub')
INTERFACE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'client','client_stub')
PROTO_FILES_LOC = os.path.join(os.path.dirname(os.path.realpath(__file__)),'proto')

def generate_proto(path,file):
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
            with open(os.path.join(path,'__init__.py'),'w') as fp:
                pass
        except Exception as e:
            print('Could not create the path because:',e)
            exit(1)
    protoc.main((
        '',
        '-Iproto',
        '--python_out='+path,
        '--grpc_python_out='+path,
        './proto/'+file,
    ))

def list_proto_files():
    files = os.listdir(PROTO_FILES_LOC)
    return files


def main():
    files = list_proto_files()
    for file in files:
        generate_proto(SERVER_PATH, file)
        generate_proto(INTERFACE_PATH,file)

if __name__=='__main__':
    main()