//console.log("działa");const 
//1. Sposób pobierania elemmentów - querySelector
const h2Band = document.querySelector("div#band h2.w3-wide");
const bandBox = document.querySelector("div#band");
const snapchatIcon = document.querySelector("footer i:nth-child(3)")

const div =document.querySelector("div");
console.log(div);

//2. Sposób pobierania elemmentów - querySelectorAll

const div2 = document.querySelectorAll("div");
console.log(div2);

//3. Sposób pobierania elementów - getElementByClassName

const specialBtn = document.getElementsByClassName("special");
console.log(specialBtn);

//4.Sposób pobierania elemntów - getElementById

const navDemoElement = document.getElementById("navDemo");
console.log(navDemoElement);

//5. Sposób pobierania elementów - getElementByTagName

const imgElement = document.getElementsByTagName("img");
console.log(imgElement);