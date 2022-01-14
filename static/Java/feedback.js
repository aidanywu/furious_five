// function send(){
//     var message = document.forms["feedback"]["message"].value;
//     console.log(message);
//     var Http = new XMLHttpRequest();
//     const url = 'https://discord.com/api/webhooks/925237909320257546/GFESPOda45vQSLrw4qi_5ucqMchlzvcRuowCDDsGQi-YGJgMt03_UwllaAO2E3tdezv3';
//     Http.open("POST", url, true);
//     Http.setRequestHeader('Content-Type', 'application/json');
//     Http.send(JSON.stringify({
//         "content": message
//     }));
// }
async function send(){
    var message = document.forms["feedback"]["message"].value;
    console.log(message);
    const url = 'https://discord.com/api/webhooks/925237909320257546/GFESPOda45vQSLrw4qi_5ucqMchlzvcRuowCDDsGQi-YGJgMt03_UwllaAO2E3tdezv3';
    const res = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({"content": message})
    });
}