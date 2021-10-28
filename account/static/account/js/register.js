let $form_fields = $("input");
$form_fields.eq(1).attr("placeholder", "Имя пользователя...");
$form_fields.eq(2).attr("placeholder", "Ваша почта...");
$form_fields.eq(3).attr("placeholder", "Пароль...");
$form_fields.eq(4).attr("placeholder", "Повторите пароль...");

$form_fields.addClass("form-control");
