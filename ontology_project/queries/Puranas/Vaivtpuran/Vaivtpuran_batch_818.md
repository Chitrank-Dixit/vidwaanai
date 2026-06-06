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

### Verse 1 (Vaivtpuran 543.14674)
- **Original**: उस समय राधाकी चतुर सखी रत्रमालाने जो मालतीवनमें घूमती फिरीं। कभी क्षणभरके लिये
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14675)
- **Original**: सबके द्वारा सम्मानित थी, श्रीकृष्णसे नीतिका बैठ जातीं, कभी उठ जातीं और कभी भूतलपर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14676)
- **Original**: सारभूत परम उत्तम मधुर वचन कहा। सो जाती थीं। कुछ क्षणोंतक अत्यन्त उच्चस्वरसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14677)
- **Original**: ।._ रत्रमाला बोली--श्रीकृष्ण ! सुनो। मैं ऐसी बारंबार रोदन और बिलाप करती रहीं। 'हे नाथ!
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14678)
- **Original**: बात बताती हूँ, जो परिणाममें सुख देनेबाली, आओ-आओ।(' ऐसा बारंबार कहकर वे संतापसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14679)
- **Original**: हितकारक, सत्य, नीतिका सारभूत तथा पति- मूर्च्छित हो गयीं। विरहानलसे संतप्त हो घास-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14680)
- **Original**: पत्नीमें प्रीति बढ़ानेवाली है। वह नीतिसम्मत, वेदों 'फूससे ढके हुए भूतलपर इस तरह गिरी, मानो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14681)
- **Original**: और पुराणोंद्वारा अनुमोदित, लोक-व्यवहारमें प्राणान्त हो गया हो। प्रशंसनीय तथा उत्तम यशकी प्राप्ति करानेवाली ब्रह्मम्‌! उस समय वहाँ अगणित गोपियाँ है। नारियोंको जैसे माता प्यारी होती है, उसी आ पहुँचीं। किन्हींके हाथोंमें चँॉबर थे और कोई
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14682)
- **Original**: तरह बन्धुजनोंमें भाई प्रिय होता है। भाईसे प्रिय चन्दनका अनुलेपन लिये आयी थीं। उन सबके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14683)
- **Original**: पुत्र और पुत्रसे प्रिय पति होता है। साध्वी बीच जो प्रियाली (प्यारी सखी) थी, उसने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14684)
- **Original**: स्त्रियोंके लिये सत्पुरुषोंद्रारा समादृत स्वामी सौ श्रोराधाकों अपनी छातीसे लगा लिया। बह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14685)
- **Original**: पुत्रोंसे भी अधिक प्रिय होता है। रसिका और प्रियाजीको मरणासन्न-सी देख प्रेमसे विह्लल हो चतुरा स्त्रियोंक लिये पतिसे बढ़कर प्यारा दूसरा रोने लगी। उसने पड्टेके ऊपर सजल कमलदल
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14686)
- **Original**: कोई नहीं है। इस मिथ्या संसारमें पति-पत्नीकी बिछाकर उसपर श्रीराधाको सुलाया। बे चेष्टाहीन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14687)
- **Original**: परस्पर प्रीति, समता तथा प्रेम-सौभाग्य परम और मृतक-सी जान पड़ती थीं। गोपियाँ सुन्दर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14688)
- **Original**: अभीष्ट है। जिस-जिस घरमें पति-पत्नी एक- श्वेत चँवर डुलाती हुई उनकी सेवामें लग गयां।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14689)
- **Original**: दूसरेके प्रति समभाव नहीं रखते, वहीं दरिद्रताका उनके अब्ोमें चन्दकका लेप किया। उस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14690)
- **Original**: निवास है। वहाँ उन दोनोंका जीवन निष्फल है*। अवस्थामें सती राधाके वस्त्र गीले हो गये थे।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14691)
- **Original**: स्त्रोके लिये स्वामीसे मतभेद या फूट होना महान्‌ इतनेमें ही श्रीकृष्ण वहाँ लौट आये और अपनी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14692)
- **Original**: दुःखकी बात है। बैसा जीवन शोक और संतापका उन प्राणवल्लभाको पूर्वोक्त अवस्थामें देखा। नारद!
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14693)
- **Original**: बीज तथा मरणसे भी अधिक कष्टदायक है। जब वे पास आने लगे तो बलवती गोपियोंने सोते और जागते समय भी स्त्रियोंके प्राण पतिमें उन्हें रोक दिया और उन्हें इस तरह पकड़कर ही बसते हैं। पति ही इहलोक और परलोकमें ले आयी, जैसे राजभय आदिसे प्रेरित हो किसी
- **Translation**: 

---

