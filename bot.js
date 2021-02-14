const Discord = require('discord.js');
const fs = require('fs');
const Reaction = require('./reaction_emoji.js');
const client = new Discord.Client();
let token = "";

try {
	token = fs.readFileSync('./token.txt', 'utf-8', (err, data) => {
		if (err)
			return "";
		return data;
	});
} catch (error) {
	throw err;
}

client.login(token);

client.on('message', message => {
	let r = new Reaction(message.author.id, message.content);

	let emojis = r.reactions;
	if (emojis.length !== 0)
		emojis.forEach((e) => { message.react(e); });
});
