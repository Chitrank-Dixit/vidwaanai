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

### Verse 1 (Vaivtpuran 16.3454)
- **Original**: हैं, फिर क्रमशः: बाल एवं प्रचण्ड-अवस्थामें या अमरत्वको भी तुच्छ माना है। इद्धत्व या
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3455)
- **Original**: आकर अन्तमें पुनः अस्त हो जाते हैं। कालक्रमसे कुबेरत्वकों तो बे कुछ गिनते ही नहीं हैं। तुम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3456)
- **Original**: जब दुर्दिन (बर्षाका समय) आता है, तब उन्हें वही परम वैष्णव श्रीकृष्ण-भक्त पुरुष हो; तुम्हारे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3457)
- **Original**: दिनमें ही छिप जाना पड़ता है। राहुसे ग्रस्त लिये देवताओंका राज्य भ्रममात्र है। उसमें तुम्हारी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3458)
- **Original**: होनेपर सूर्य काँपने लगते हैं; पुनः थोड़ी देरके क्या आस्था हो सकती है ? राजन्‌! तुम देवताओंका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3459)
- **Original**: बाद प्रसन्नता आ जाती है। राज्य उन्हें लौटा दो और मुझे आनन्दित करो।। राजन! पूर्णिमाकी रातमें चन्द्रमा जैसे अपनी तुम अपने राज्यमें सुखसे रहो और देवता अपने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3460)
- **Original**: सभी कलाओंसे पूर्ण रहते हैं, बैसे ही सदा नहीं स्थानपर रहें। भाई-भाईमें विरोधसे कोई लाभ [रहते। प्रतिदिन क्षीण होते रहते हैं। फिर नहीं है; तुम सब-के-सब एक ही पिता कश्यपजीके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3461)
- **Original**: अमाबास्याके बाद बे प्रतिदिन पुष्ट होने लगते वंशज हो। ब्रह्महत्या आदिसे उत्पन्न हुए जितने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3462)
- **Original**: हैं। शुक्लपक्षमें वे शोभा-सम्पत्तिसे युक्त रहते और पाप हैं, उनकी यदि जातिद्रोह-सम्बन्धी पापोंसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3463)
- **Original**: कृष्णपक्षमें क्षय-रोगसे पुनः म्लान हो जाते हैं। तुलना की जाय तो बे इनकी सोलहरवी कलाके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3464)
- **Original**: ग्रहणके अवसरपर उनकी शोभा नष्ट हो जाती बराबर भी नहीं हो सकते। है तथा दुर्दिन आनेपर अर्थात्‌ मेघाच्छन्न आकाशमें राजेन्द्र! यदि तुम अपनी सम्पत्तिकी हानि वे नहीं चमक पाते। काल-भेदके अनुसार चन्द्रमा समझते हो तो भला, सोचो तो कौन ऐसे पुरुष
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3465)
- **Original**: किसी समय शुद्ध-श्रीसम्पन्न होते हैं तो किसी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3466)
- **Original**: + प्रकृतिखवण्ड « 157 555#$$5555*5$5 5 5445 5 4 # # 55 # 8 # 58% 6 ## 5 888 44686 8& 44 414 544 444 $ 5 $ 4 $ 4 5 % 5 44 45 4555 4 5 %. समय श्रीहीन हो जाते हैं। बलि भविष्यमें इन्द्र
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3467)
- **Original**: आपने यहाँ जातिद्रोहकों जो महान्‌ पाप बताया है, होंगे। यद्यपि इस समय श्रीहीन होकर ये सुतल-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3468)
- **Original**: वह यदि देवताओंको मान्य है तो राजा बलिका लोकमें स्थित हैं। समयपर विश्व नष्ट होते हैं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3469)
- **Original**: सर्वस्व छीनकर उन्हें सुतललोकमें क्यों भेज दिया और कालके प्रभावसे पुनः उनकी उत्पत्ति भी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3470)
- **Original**: गया? मैंने यह सारा ऐश्वर्य अपने पराक्रमसे प्राप्त होती है। अखिल चराचर प्राणी कालकी प्रेरणाके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3471)
- **Original**: किया है--दानवोंके पूर्ववैभवका उद्धार किया है। अनुसार नष्ट और उत्पन्न होते हैं। केवल परमात्मा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3472)
- **Original**: भगवान्‌ गदाधर भी सुतललोकसे दानवसमाजको श्रीकृष्ण ही सम हैं; क्योंकि वे ही सबके ईश्वर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3473)
- **Original**: हटा देनेमें समर्थ नहीं हैं; क्योंकि वह उनका हैं। उन्हींकी कृपासे मुझे भी 'मृत्यु्य' होनेका
- **Translation**: 

---

