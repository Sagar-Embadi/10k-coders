let card= document.getElementById("card1")
card.style.width="600px"
card.style.padding="20px"
card.style.backgroundColor="grey"
card.style.borderRadius="20px"
card.style.textAlign="center"
card.style.margin="auto"

card.innerHTML=`<img src=${'https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823__340.jpg'} width='100%'>
                <h2>Nature does not hurry, yet everything is accomplished.</h2>
                <p> Nature is like our mother; it nourishes and nurtures us. All our basic necessities are fulfilled by nature. Whether it’s the air we breathe, the land we live on, the water we drink or the food we eat, it all comes from nature</p>`

let card2=document.getElementById("card2");
card2.style.width="600px"
card2.style.padding="20px"
card2.style.backgroundColor="slategrey"
card2.style.borderRadius="20px"
card2.style.margin="50px auto"
card2.style.display="flex"
card2.style.gap="20px"

card_child1=document.createElement("div");
card_child2=document.createElement('div')
card2.appendChild(card_child1)
card2.appendChild(card_child2)
card_child1.innerHTML=`<img src=${'https://wallpapercave.com/wp/wp1869540.jpg'} width='300px' height='200px'>
                        <h2>Cars</h2>`
card_child2.innerHTML=`<img src=${'https://hips.hearstapps.com/autoweek/assets/s3fs-public/60523009-7.jpg'} width='100%' height='200px'>
                        <h2>Cars</h2>`

let card3=document.getElementById("card3");
card3.style.width="600px"
card3.style.padding="20px"
card3.style.backgroundColor="skyblue"
card3.style.borderRadius="20px"
card3.style.margin="auto"
card3.style.display="flex"
card3.style.gap="20px"
card3.style.flexWrap="wrap"


let data=[{image:'https://th.bing.com/th/id/OIP.GwpMebDFiZAfVdoNsobrgAHaHa?rs=1&pid=ImgDetMain',h1:'Smile'},{image:'https://th.bing.com/th/id/OIP.9oLZAPHl-RQsAgEhPQktKgAAAA?pid=ImgDet&w=184&h=184&c=7&dpr=1.3',h1:'Sad'},{image:'https://cdn.shopify.com/s/files/1/1061/1924/products/Super_Angry_Face_Emoji_ios10_large.png?v=1542436021',h1:'Angry'}]
for(i=0;i<data.length;i++){
    let card_child=document.createElement('div')
    card_child.innerHTML=`<img src='${data[i].image}' width='250px' >
                    <h1>${data[i].h1}</h1>`
    card3.appendChild(card_child)
}