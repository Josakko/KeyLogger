const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");
const readline = require("readline");
const os = require('os');
const { get } = require("http");

let request = 0
function getIp() {
    const networkInterfaces = os.networkInterfaces();
    let ip;
    Object.keys(networkInterfaces).forEach((interfaceName) => {
      const interfaces = networkInterfaces[interfaceName];
      for (let i = 0; i < interfaces.length; i++) {
        const iface = interfaces[i];
        if (iface.family === 'IPv4' && !iface.internal) {
          ip = iface.address;
          break;
        }
      }
    });
    return ip;
}

const app = express();
app.use(bodyParser.json({extended: true}));

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter the port to use: ", function(port) {
    app.post("/", (req, res) => {
        request = request + 1
        console.log(`Request number ${request} received`);
        fs.writeFileSync(`log.txt`, req.body.content);
        res.send()
    });

    app.listen(port, () => {
        console.log(`Listening on port ${port}, Ip: ${getIp()}, use ^C to exit`);
    });

    rl.close();
});
