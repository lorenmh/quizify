#!/usr/local/bin/node

var exec = require('child_process').exec,
    fs = require('fs')
;

var PATH = './input.txt'
;

var numLines = new Promise((res, rej) => {
  exec(`wc ${PATH}`, (err, data) => {
    if (!err) {
      res(+ data.match(/(\d)/)[1]);
    } else {
      rej(err);
    }
  });
});

var read = new Promise((res, rej) => {
  fs.readFile(PATH, (err, data) => {
    if (!err) {
      res(data);
    } else {
      rej(err);
    }
  });
});

var write = function (data) {
  return new Promise((res, rej) => {
    fs.writeFile(PATH, data, (err) => {
      if (!err) {
        res();
      } else {
        rej(err);
      }
    });
  });
}

function definition(line) {
  var commaIndex = line.indexOf(',');
  if (commaIndex >= 0) {
    return [line.substr(0,commaIndex), line.substr(commaIndex + 1)];
  } else {
    return [line, null];
  }
}

function toLines(file) {
  return String.prototype.split.call(file, '\n').filter((l) => l.length);
}

function setDefinition(lines, index, newDef) {
  var def = definition(lines[index]);
  def[1] = newDef;
  lines[index] = def.join(',');
}

read.then((file) => {
  var lines = toLines(file);
  var index = Math.floor(Math.random() * lines.length);
  var def = definition(lines[index]);
  var stdin;
  
  console.log(`The word is: ${def[0]}`);

  if (!def[1]) {
    console.log('Definition not set, enter definition:');
    stdin = process.openStdin();
    var newDef = '';
    stdin.addListener('data', (d) => {
      newDef += d;
      setDefinition(lines, index, newDef.replace(/\n|\r\n/, ''));
      write(lines.filter((l) => l.match(/\w/)).join('\n'))
        .then(() => process.exit(0));
    })
  } else {
    console.log('Press enter to see the definition.');
    stdin = process.openStdin();
    stdin.addListener('data', (d) => {
      console.log(def[1]);
      process.exit(0);
    });
  }
}).catch((error) => {
  console.log(`ERROR: ${error}`);
});
