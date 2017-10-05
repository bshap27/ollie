$(document).ready(function(){
		// for each form field with class 'fieldWrapper[i]', on change, unhide the next form field.
		$("div.fieldWrapper input").on('keypress', function(){
			var elm = $(this).parents('.fieldWrapper'),
					idx = parseInt($(elm).attr('id').split('-')[1])
					nextIdx = idx + 1
					nextId = '#field-' + nextIdx
					next = $(nextId);
			$(this).css('border-bottom', '1px solid #000000')
			next.removeClass('hide')
		})
})