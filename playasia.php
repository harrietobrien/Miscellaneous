<?php

function pa_convert_link( $_link )
{
  $parts = parse_url( $_link );
  $query = Array();
  #  parse_str( $parts[ 'query' ], $query );	  
  $query[ 'tagid' ] = 5163631;
  $query = http_build_query( $query );

  $_link = "$parts[scheme]://$parts[host]$parts[path]?$query";
    if ( isset( $parts[ 'fragment' ] ) )
      $_link .= "#$parts[fragment]";
	return $_link;
}

$links = array_slice($argv, 1);
var_dump($links);
$out = fopen("links.txt", "w") or die ("error");
foreach ($links as $link) {
  $new_link = pa_convert_link($link);
  fwrite($out, $link . PHP_EOL);
  print_r($new_link . PHP_EOL);
}
fclose($out);
unset($link)
?>
