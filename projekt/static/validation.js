document.querySelectorAll('form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
        var valid = true;
        form.querySelectorAll('input[required], textarea[required]').forEach(function (field) {
            var val = (field.value || '').trim();
            if (!val) {
                field.classList.add('is-invalid');
                valid = false;
                return;
            }
            if (field.minLength > 0 && val.length < field.minLength) {
                field.classList.add('is-invalid');
                valid = false;
                return;
            }
            if (field.type === 'date' && !/^\d{4}-\d{2}-\d{2}$/.test(val)) {
                field.classList.add('is-invalid');
                valid = false;
                return;
            }
            field.classList.remove('is-invalid');
        });
        if (!valid) {
            e.preventDefault();
        }
    });
});
