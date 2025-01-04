let form=document.getElementById("register")

form.addEventListener("submit",(s)=>{
    s.preventDefault()
    let name=document.getElementById("name").value;
    let email=document.getElementById("email").value;
    let pass=document.getElementById("password").value;
    // console.log(name,email,pass);
    localStorage.setItem("userinfo",JSON.stringify({"name":name,"email":email,"password":pass}))
    location.href="./login.html"
})