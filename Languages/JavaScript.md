# JavaScript
## Hello World
```javascript
document.write("<!DOCTYPE><html><head><title>Hello World!</title><body><div>Hello World!</div></body></html>");
```

## View Device & Browser Name
```javascript
var os = [
    { name: 'Windows Phone', value: 'Windows Phone', version: 'OS' },
    { name: 'Windows', value: 'Win', version: 'NT' },
    { name: 'iPhone', value: 'iPhone', version: 'OS' },
    { name: 'iPad', value: 'iPad', version: 'OS' },
    { name: 'Kindle', value: 'Silk', version: 'Silk' },
    { name: 'Android', value: 'Android', version: 'Android' },
    { name: 'PlayBook', value: 'PlayBook', version: 'OS' },
    { name: 'BlackBerry', value: 'BlackBerry', version: '/' },
    { name: 'Macintosh', value: 'Mac', version: 'OS X' },
    { name: 'Linux', value: 'Linux', version: 'rv' },
    { name: 'Palm', value: 'Palm', version: 'PalmOS' }
];

var browser = [
    { name: 'Chrome', value: 'Chrome', version: 'Chrome' },
    { name: 'Firefox', value: 'Firefox', version: 'Firefox' },
    { name: 'Safari', value: 'Safari', version: 'Version' },
    { name: 'Internet Explorer', value: 'MSIE', version: 'MSIE' },
    { name: 'Opera', value: 'Opera', version: 'Opera' },
    { name: 'BlackBerry', value: 'CLDC', version: 'CLDC' },
    { name: 'Mozilla', value: 'Mozilla', version: 'Mozilla' }
];

var header = [
    navigator.platform,
    navigator.userAgent,
    navigator.appVersion,
    navigator.vendor,
    window.opera
];

function matchItem(string, data) {
    var i = 0,
        j = 0,
        html = '',
        regex,
        regexv,
        match,
        matches,
        version;
    
    for (i = 0; i < data.length; i += 1) {
        regex = new RegExp(data[i].value, 'i');
        match = regex.test(string);
        if (match) {
            regexv = new RegExp(data[i].version + '[- /:;]([\d._]+)', 'i');
            matches = string.match(regexv);
            version = '';
            if (matches) { if (matches[1]) { matches = matches[1]; } }
            if (matches) {
                matches = matches.split(/[._]+/);
                for (j = 0; j < matches.length; j += 1) {
                    if (j === 0) {
                        version += matches[j] + '.';
                    } else {
                        version += matches[j];
                    }
                }
            } else {
                version = '0';
            }
            return {
                name: data[i].name,
                version: parseFloat(version)
            };
        }
    }
    return { name: 'unknown', version: 0 };
}

var agent = header.join(' ');
var os = this.matchItem(agent, os);
var browser = this.matchItem(agent, browser);


document.write('<div>navigator.platform = ' + navigator.platform + "</div>");
var os_ver = navigator.userAgent;
if(os_ver.indexOf('iPhone OS') != -1) {
	os_ver = os_ver.substring(os_ver.indexOf('iPhone OS'), os_ver.indexOf(')'));
} else if (os_ver.indexOf('Mac OS X') != -1) {
	os_ver = os_ver.substring(os_ver.indexOf('Mac OS X'), os_ver.indexOf(')'));
} else {
	os_ver = "Unknown";
}
document.write("<div>navigator.userAgent = " + os_ver + "</div>");
document.write("<div>navigator.userAgent (full) = " + navigator.userAgent + "</div>");
document.write("<div>os.name = " + os.name + "</div>");
document.write("<div>os.version = " + os.version + "</div>");
document.write("<div></div>");
document.write("<div>browser.platform = " + browser.platform + "</div>");
document.write("<div>navigator.platform = " + navigator.platform + "</div>");
```
