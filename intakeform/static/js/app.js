$(document).ready(function(){

		$('#show_intake_form').on('click', function(){
			$(this).css('display','none')
			$('form[action="intake_form/"]').removeClass('hide')
		})

		// for each form input field with class 'fieldWrapper[i]', on change, unhide the next form field.
		$("div.fieldWrapper input").on('keypress', function(){
			if ($(this).attr('id') != 'id_breed_1') {	
				showNextField(this);
			}
		})

		// can't apply the above function generally to all SELECTS because of cascading conditional selections
		$("div.fieldWrapper select").on('change', function(){
			var select_whitelist = ['id_fixed', 'id_active', 'id_weight', 'id_build']
			if (select_whitelist.indexOf($(this).attr('id')) > -1) {
				showNextField(this);
			}
		})

		function findNextField(changed, index_inc = 1) {
			var elm = $(changed).parents('.fieldWrapper')
					idx = parseInt($(elm).attr('id').split('-')[1])
					nextIdx = idx + index_inc
					nextId = '#field-' + nextIdx;
			return $(nextId);
		}

		function showNextField(changed, index_inc = 1) {
			next = findNextField(changed, index_inc)
			$(changed).css('border-bottom', '1px solid rgb(230, 46, 37)')
			if (next.length > 0) {
				next.removeClass('hide')
			} //else { // reached the last form field
				// $('button[type="submit"]').removeClass('hide')
			// }
			if (findNextField(changed, 2).length == 0) {
				$('button[type="submit"]').removeClass('hide') // show submit button when you've reached second to last field, since the last field is pre-populated.
			}
		}

		// add pet's name to fields once it is populated
		$('input#id_pups_name').on('change', function(){
			var pet_name = $('input[name="pups_name"]').val()
			$('label[for="id_breed_type"]').text(pet_name + ' is a')
			$('label[for="id_sex"]').text(pet_name + ' is a')
			$('label[for="id_birth"]').text(pet_name + ' was born in')
			$('label[for="id_active"]').text('I would describe ' + pet_name + ' as')
			$('label[for="id_weight"]').text(pet_name + ' is about')
			$('label[for="id_build"]').text('I would describe ' + pet_name + '\'s build as')
			$('label[for="id_allergies"]').text(pet_name + ' is allergic to')
			// $('label[for="id_eats"]').text(pet_name + ' currently eats')
		})

		// show appropriate # of breed fields depending on mix selection
		$('select#id_breed_type').on('change', function(){
			var selection = $('select#id_breed_type').val()
			switch(selection) {
		    case 'single':
	        showNextField(this);
	        $('#id_breed_2').parents('div.fieldWrapper').addClass('hide');
	        hideFutureEmptyField('#id_sex')
	        break;
		    case 'double':
	        showNextField(this);
	        showNextField(this, 2);
	        hideFutureEmptyField('#id_sex')
	        break;
		    default:
		    	$('#id_breed_1').parents('div.fieldWrapper').addClass('hide');
	        $('#id_breed_2').parents('div.fieldWrapper').addClass('hide');
	        showNextField(this, 3);
	        break;
			}
		});
		
		$('input#id_breed_1').on('keypress', function(){
			if ($('select#id_breed_type').val() == 'single'){
				showNextField(this, 2);
			}
		})

		function hideFutureEmptyField(field_id) {
			if ($(field_id).val() == '') {
				$(field_id).parents('div.fieldWrapper').addClass('hide');
			}
		}

		// dynamically append 'fixed' language based on pet's gender.
		$('select#id_sex').on('change', function(){
			var selection = $(this).val(),
				word = selection == 'M' ? 'neutered' : 'spayed',
				blank = new Option('', ''),
				yes = new Option(word, 'Y'),
				no = new Option('not ' + word, 'N');
			$('select#id_fixed option').remove()
			$('select#id_fixed').append($(blank)).append($(yes)).append($(no));
			showNextField(this);
		})
})