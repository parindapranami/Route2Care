var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var medicineId = this.dataset.medicine
        var action = this.dataset.action
        console.log('medicineId:', medicineId, 'action:',action)

        console.log('USER:',user)
        if (user == 'AnonymousUser'){
            addCookieItem(medicineId, action)
        }else{
            // console.log('User is authenticated, sending data...')
            updateUserOrder(medicineId,action)
        }
    })
}



function updateUserOrder(medicineId, action){
    console.log('User is authenticated, sending data...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'medicineId':medicineId, 'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:',data)
        location.reload()
    });
}

function addCookieItem(medicineId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[medicineId] == undefined){
		cart[medicineId] = {'quantity':1}

		}else{
			cart[medicineId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[medicineId]['quantity'] -= 1

		if (cart[medicineId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[medicineId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}
