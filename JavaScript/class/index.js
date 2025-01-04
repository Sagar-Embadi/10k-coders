let form=document.getElementById("register")

form.addEventListener("submit",(s)=>{
    s.preventDefault()
    let name=document.getElementById("name").value;
    let email=document.getElementById("email").value;
    let pass=document.getElementById("password").value;
    // console.log(name,email,pass);
    localStorage.setItem("userinfo",JSON.stringify({"name":name,"email":email,"password":pass}))
})

let grand=document.getElementById("grand")
let parent=document.getElementById("parent")
let child=document.getElementById("child")

// grand.addEventListener("click",(e)=>{
//     e.stopPropagation()
//     console.log("Grand Clicked");
    
//     grand.style.backgroundColor="red"

// })
// parent.addEventListener("click",(e)=>{
//     e.stopPropagation()
//     console.log("Parent Clicked");

//     parent.style.backgroundColor="blue"

// })
// child.addEventListener("click",(e)=>{
//     e.stopPropagation()
//     console.log("Child Clicked");

//     child.style.backgroundColor="yellow"

// })



// grand.addEventListener("click",(e)=>{
//     e.stopPropagation()
//     console.log("Grand Clicked");
    
//     grand.style.backgroundColor="red"

// },true)
// parent.addEventListener("click",(e)=>{
//     e.stopPropagation()
//     console.log("Parent Clicked");

//     parent.style.backgroundColor="blue"

// },true)
// child.addEventListener("click",(e)=>{
//     e.stopPropagation()
//     console.log("Child Clicked");

//     child.style.backgroundColor="yellow"

// },true)