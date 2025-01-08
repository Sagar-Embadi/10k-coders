let card_container=document.getElementById("card_container")
let mens=document.getElementById("mens")
let women=document.getElementById("women")
let electronics=document.getElementById("electronics")
let jewelry=document.getElementById("jewelry")

mens.addEventListener("click",()=> project("men's clothing"))
women.addEventListener("click",()=> project("women's clothing"))
electronics.addEventListener("click",()=> project("electronics"))
jewelry.addEventListener("click",()=> project("jewelery"))

async function project(cat=null) {
    let apiData=await fetch("https://fakestoreapi.com/products")
    let productList=await apiData.json()
    // console.log(productList)

    let filteredData= cat ? res=productList.filter(x=> x.category == cat) : productList
    console.log(filteredData);
    card_container.innerHTML=""
    filteredData.forEach(x =>{
        let card=document.createElement("div")
        card.className="card"
        card.innerHTML=`
            <img src=${x.image} alt="${x.title}">
            <p>${x.title}</p>
            <span>PRICE: ${x.price}</span>
            <button id="addToCart">Add to Cart</button>
            <button id="buyNow">Buy Now</button>
        `
        card_container.appendChild(card)
        card.addEventListener("click",()=>{
            location.href="./single.html"
            localStorage.setItem("singleP",JSON.stringify(x))
        })
        card.querySelector("#addToCart").addEventListener("click",(e)=>{
            e.stopPropagation()
            Swal.fire('Product Added to Card', 'Continue your Shopping Now', 'success');
            let cartItems= JSON.parse(localStorage.getItem("cartItems")) || []
            cartItems.push(x)
            localStorage.setItem("cartItems",JSON.stringify(cartItems))
        })
        card.querySelector("#buyNow").addEventListener("click",(e)=>{
            e.stopPropagation()
            location.href="./cart.html"
        })
    });
}
project()