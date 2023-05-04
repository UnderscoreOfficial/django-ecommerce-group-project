const gulp = require('gulp');

gulp.task('copy-pico', function () {
    return gulp
        .src('node_modules/@picocss/pico/css/pico.min.css*')
        .pipe(gulp.dest('static/src/css'));
});
