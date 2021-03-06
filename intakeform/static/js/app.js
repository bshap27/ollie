$(document).ready(function(){

		function showIntakeForm(){
			$('#show_intake_form').css('display','none')
			$('form[action="intake_form/"]').removeClass('hide')
		}
		
		$('#show_intake_form').on('click', function(){
			showIntakeForm()
		})

		// for each form input field with class 'fieldWrapper[i]', on change, unhide the next form field.
		$("div.fieldWrapper input").on('keypress', function(){
			if ($(this).attr('id') != 'id_breed1') {	
				showNextField(this);
			}
		})

		// can't apply the above function generally to all SELECTS because of cascading conditional selections
		$("div.fieldWrapper select").on('change', function(){
			var select_blacklist = ['id_sex']
			if (select_blacklist.indexOf($(this).attr('id')) == -1) {
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
			updatePetName()
		})

		function updatePetName() {
			var pet_name = $('input[name="pups_name"]').val()
			$('label[for="id_breed_type"]').text(pet_name + ' is')
			$('label[for="id_sex"]').text(pet_name + ' is a')
			$('label[for="id_birth"]').text(pet_name + ' was born in')
			$('label[for="id_active"]').text('I would describe ' + pet_name + ' as')
			$('label[for="id_weight"]').text(pet_name + ' is about')
			$('label[for="id_build"]').text('I would describe ' + pet_name + '\'s build as')
			$('label[for="id_allergies"]').text(pet_name + ' is allergic to')
			// $('label[for="id_eats"]').text(pet_name + ' currently eats')
		}

		// show appropriate # of breed fields depending on mix selection
		$('select#id_breed_type').on('change', function(){
			var selection = $('select#id_breed_type').val()
			switch(selection) {
		    case 'single':
	        showNextField(this);
	        $('#id_breed2').parents('div.fieldWrapper').addClass('hide');
	        hideFutureEmptyField('#id_sex')
	        break;
		    case 'double':
	        showNextField(this);
	        showNextField(this, 2);
	        hideFutureEmptyField('#id_sex')
	        break;
		    default:
		    	$('#id_breed1').parents('div.fieldWrapper').addClass('hide');
	        $('#id_breed2').parents('div.fieldWrapper').addClass('hide');
	        showNextField(this, 3);
	        break;
			}
		});
		
		$('input#id_breed1').on('keypress', function(){
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
				yes = new Option(word, "True"),
				no = new Option('not ' + word, "False");
			$('select#id_fixed option').remove()
			$('select#id_fixed').append($(blank)).append($(yes)).append($(no));
			showNextField(this);
		})

		$(window).keydown(function(event){ // don't submit form on enter
	    if(event.keyCode == 13) {
	      event.preventDefault();
	      return false;
	    }
	  });

		// when redirect to form with validation, do the following:

		// show form automatically
		if ($("div.fieldWrapper input, div.fieldWrapper select").val().length > 0) {
			showIntakeForm()
		}

		// populate pet's name if already entered
		if ($('input[name="pups_name"]').val().length) {
			updatePetName()
		}

		// show all fields that have entries plus the next empty field
		$("div.fieldWrapper input, div.fieldWrapper select").each(function(){
			if ($(this).val().length){
				showNextField(this,0);
				var blacklist = ['id_breed1', 'id_breed_type']
				if (blacklist.indexOf($(this).attr('id')) == -1) {
					showNextField(this);
				}
			}
		})

})