const Chance = require('chance');

const chance = new Chance();

console.log("Name:", chance.name());
console.log("First Name:", chance.first());
console.log("Last Name:", chance.last());
console.log("Age:", chance.age());
console.log("Email:", chance.email());
console.log("Phone:", chance.phone());