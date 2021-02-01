const PROTO_PATH = "./definitions/tree.proto";

var parseArgs = require("minimist");
var grpc = require("@grpc/grpc-js");
var protoLoader = require("@grpc/proto-loader");

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});
var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);

function main() {
  var argv = parseArgs(process.argv.slice(2), {
    string: "n",
  });
  var n = null;
  if (argv._.length > 0) {
    n = argv._[0];
  }
  var target = "localhost:50051";

  var client = new protoDescriptor.protoTrees.TreeService(
    target,
    grpc.credentials.createInsecure()
  );

  client.getTrees({ n: n }, function (err, response) {
    console.log(response, err);
  });
}

main();
