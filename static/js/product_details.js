const lens = document.querySelector('.magnifier-lens');
const product_img = document.querySelector('.product-img img');
const magnified_img = document.querySelector(".magnified-img");

function magnify(product_img, magnified_img){
    product_img.addEventListener('mousemove', moveLens)
    lens.addEventListener('mousemove', moveLens)
    lens.addEventListener("mouseout", leaveLens )
}

function moveLens(e){
    let x, y , cx, cy;

    /* Get the position of cursor */
    // console.log("X: " , e.pageX , " Y: ", e.pageY);
    const product_img_rect = product_img.getBoundingClientRect();
    x = e.pageX - product_img_rect.left -lens.offsetWidth/2;
    y = e.pageY - product_img_rect.top - lens.offsetHeight/2;

    let max_x_pos = product_img_rect.width - lens.offsetWidth;
    let max_y_pos = product_img_rect.height - lens.offsetHeight;

    /* prevent lens go out of image */
    if(x > max_x_pos) x = max_x_pos;
    if(x < 0) x = 0;
    if(y > max_y_pos) y = max_y_pos;
    if(y < 0) y = 0;

    /* set lens position */
    lens.style.cssText = `top: ${y}px; left: ${x}px;`

    /* Calculate the magnified image and lens aspect ratio */
    cx = magnified_img.offsetWidth / lens.offsetWidth;
    cy = magnified_img.offsetHeight/ lens.offsetHeight;

    magnified_img.style.cssText = `
            background:
                url(${product_img.src})
                -${x * cx}px -${y * cy}px /
                ${product_img_rect.width * cx}px ${product_img_rect.height * cy}px
                no-repeat;

    `;
    lens.classList.add("active");
    magnified_img.classList.add("active");
}
function leaveLens(){
    lens.classList.remove("active");
    magnified_img.classList.remove("active");

}

magnify(product_img, magnified_img)


function setImage(id) {

        let src = document.getElementById(id).firstElementChild.src
        let zoom_image = document.getElementById("zoom").firstElementChild
        console.log("zoom image = ", zoom_image)
        zoom_image.src = src
        console.log("zoom image = ", zoom_image)
}
