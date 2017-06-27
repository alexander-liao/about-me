function gen_mail_to_link(id, lhs, rhs) {
  LHS = '';
  for (var x = 0; x < lhs.length; x++) {
    LHS += lhs.charAt(x * x);
  }
  document.getElementById(id).innerHTML = document.getElementById(id).innerHTML.replace("[Requires JavaScript to view]", "<a href='mailto:" + LHS + '@' + rhs + "'>" + LHS + '@' + rhs + '</a>');
}
