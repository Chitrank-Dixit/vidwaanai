# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 543.15774)
- **Original**: भी होगा। मनमें पुनः कहनेका विचार करनेपर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15775)
- **Original**: 688 + संक्षिप्त ब्रह्म॑तैवर्तपुराण * &#%#%4##& 4668 44 # # 4 6 # 48% # 8 $ 5 # 5 845 ## 688 58 $# $ ###& #4 # 5 8 $ 8 4 4 44 4 $ 6 $ # 6 6 8 8 8 $ 8
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15776)
- **Original**: 8 8 & 6 सूर्यने रोक दिया था; इसी कारण यह धर्म
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15777)
- **Original**: भूषण और सुन्दर रत्नजटित दर्पणोंसे विभूषित था। कलियुगकी समाप्तिमें कलामय हो रह जायगा।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15778)
- **Original**: उस रथको देखकर वृन्दाने हरि, शंकर, ब्रह्मा नन्दजी! इसी बोच देबताओंने बेगपूर्वक तथा समस्त देवताओंको नमस्कार किया और गोलोकसे आये हुए एक अत्यन्त सुन्दर एवं शुभ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15779)
- **Original**: फिर उसपर सवार हो बह गोलोकको चली गयी। रथको देखा। उस रथका निर्माण अमूल्य रत्रोंद्वारा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15780)
- **Original**: तत्पश्चात्‌ सभी देवता अपने-अपने स्थानकों चले हुआ था। उसमें हीरेके हार लटक रहे थे और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15781)
- **Original**: गये। अब तुम्हारी पुनः कया सुननेकी इच्छा है? वह मणि, माणिक्य, मुक्ता, वस्त्र, श्वेत चँंबर, (अध्याय 86) #पफह>+0 रथ 2222800क्‍.2+000 सनत्कुमार आदिके साथ श्रीकृष्णका समागम, सनत्कुमारके द्वारा श्रीकृष्णके रहस्योद्धाटन करनेपर नन्दजीका पश्चात्तापपूर्ण कथन तथा मूर्च्छित होना नन्दजीने कह्ा--प्रभो! आप स्वयं बेदोंके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15782)
- **Original**: [सहसा उठ खड़े हुए और हाथ जोड़कर नमस्कार अधीश्वर हैं; अतः वेद, ब्रह्मा, शिव और शेष
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15783)
- **Original**: करनेके पश्चात्‌ उन्हें आदरसहित रमणीय सिंहासनोंपर आदि देवता तथा मुनि और सिद्ध आदि आपको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15784)
- **Original**: बैठाये। फिर श्रीकृष्णने कुशल-प्रश्नपूर्वक परस्पर जाननेमें असमर्थ हैं। आप कौन हैं-यह जाननेके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15785)
- **Original**: वार्तालाप करके उनको विधिवत्‌ पूजा की और लिये मेरे मनमें प्रबल उत्कण्ठा है; अत: इस
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15786)
- **Original**: स्वयं भी उन्हींके मध्यमें आसनासीन हुए। इसी निर्जन स्थानमें आप अपना सारा वृत्तान्त यथार्थ समय श्रीकृष्णो आकाशमें एक समुज्ज्वल रूपसे वर्णन कीौजिये। ' तेजोराशि दीख पड़ी। उसे मुनियोंने भी देखा। श्रीनारायण कहते हैं--नारद! इसी बोच
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15787)
- **Original**: वत्स नारद! उस तेजके अंदर सुवर्णकौ-सी वहाँ श्रीकृष्णका दर्शन करनेके लिये सहसा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15788)
- **Original**: कान्तिवाले, पश्चवर्षीय नग्न-बालकके रूपमें पुलह, पुलस्त्य, क्रतु, भृगु, अड्भिरा, प्रचेतागण,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15789)
- **Original**: सनत्कुमारजी थे। वे सहसा उस सभाके बीच वसिष्ठ, दुर्वासा, कण्व, कात्यायन, पाणिनि,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15790)
- **Original**: प्रकट हो गये। उन्हें एकाएक सामने खड़े देखकर कणाद, गौतम, सनक, सनन्दन, तीसरे सनातन,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15791)
- **Original**: सभी मुनिवरोंने प्रणाम किया तथा श्रीकृष्णने भी कपिल, आसुरि, वायु (वोदु), पश्वशिख, विश्वामित्र,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15792)
- **Original**: मुस्कानयुक्त एवं ख्निग्ध नेत्रोंवाले कुमारकों वाल्मीकि, कश्यप, पराशर, विभाण्डक, मरीचि,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15793)
- **Original**: युक्तिपूर्वक सादर सिर झुकाया। तब सनत्कुमारजी शुक्र, अत्रि, बृहस्पति, गार्ग्य, वात्स्य, व्यास,
- **Translation**: 

---

