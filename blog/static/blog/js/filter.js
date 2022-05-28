var applied_filters = jQuery.parseJSON($("#applied_filters").text())
var searched = jQuery.parseJSON($("#searched").text())
var inputs = $("input");

console.log(searched)

console.log(applied_filters)

for (input of inputs)
{
    for (filter of applied_filters)
    {
        if (input.name == filter){
            if ((filter == "search") && (searched != '')){
                $(input).val(searched.join(' '))
            }else{
                console.log(input.name)
                $(input).prop("checked",true)
            }
        }   
    }
}

$("button[type=button]").click(function(event){
    inputs.map((index,input) => $(input).prop("checked",false))
})

$("input[name=search]").change(function(event){
    console.log(this.value)
    this.form.submit()
})
