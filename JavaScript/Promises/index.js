const mani=new Promise((l,p)=>{
    if (1){
        setTimeout(()=>{
            l("successful")
        },3000)
    }else{
        setTimeout(()=>{
            p("failed")
        },2000)
    }
})
// console.log(mani);
mani.then(ot=>console.log(ot)).catch(err=>console.log(err))