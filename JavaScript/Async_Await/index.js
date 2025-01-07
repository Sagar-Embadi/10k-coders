a()
async function a() {
  let data = await fetch("https://fakestoreapi.com/products");
  console.log(data);
  
  let allData = await data.json();

  console.log(allData);

  let card_container = document.getElementById("card_container");
  card_container.style.display = "flex";
  card_container.style.flexWrap = "wrap";
  card_container.style.gap = "30px";

  card_container.innerHTML = " ";
  allData.filter((x) => {
    let card = document.createElement("div");
    card.innerHTML = `<img src='${x.image}' width='100%' height="70%" >
                        <h2>${x.title}</h2>
                        <h4>PRICE: ${x.price}</h4>`;
    card.style.width = "300px";
    // card.style.height = "550px";
    card.style.padding = "10px";
    card.style.backgroundColor = "lightgrey";
    card_container.appendChild(card);
    card.addEventListener("click", () => {
      location.href = "./single.html";
      // console.log(x);
      localStorage.setItem("item", JSON.stringify(x));
    });
  });

  let men = document.getElementById("men");

  men.addEventListener("click", mens);
  function mens() {
    card_container.innerHTML = "";
    allData.filter((x) => {
      if (x.category === "men's clothing") {
        let card = document.createElement("div");
        card.innerHTML = `<img src='${x.image}' width='100%' height="70%" >
                                    <h2>${x.title}</h2>
                                    <h4>PRICE: ${x.price}</h4>`;
        card.style.width = "300px";
        card.style.height = "550px";
        card.style.padding = "10px";
        card.style.backgroundColor = "coral";
        card_container.appendChild(card);
        card.addEventListener("click", () => {
          location.href = "./single.html";
          localStorage.setItem("item", JSON.stringify(x));
        });
      }
    });
  }
}


