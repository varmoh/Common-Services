Handlebars.registerHelper('formatDate', function(dateString) {
    const [year, month, day] = dateString.split('-');
    return `${day}.${month}.${year}`;
  });