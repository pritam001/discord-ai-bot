require("dotenv").config();

console.log(process.env.PING_JS_BOT_TOKEN);

const {Client} = require("discord.js");
const client = new Client();

client.on("ready", () => {
    console.log(`${client.user.username} is connected`);
});

client.on("message", (message) => {
    if(message.author.bot) {
        return ;
    } else {
        if(message.content === "hello") {
            message.channel.send("hello");
        }
    }
})

client.login(process.env.PING_JS_BOT_TOKEN).then(r => console.log(r));
