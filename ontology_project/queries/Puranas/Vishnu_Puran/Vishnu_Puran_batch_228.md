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

### Verse 1 (Vishnu Puran 0.4541)
- **Original**: हमारे आचार्यजीफे समान अद्वैत-संस्कारयुक्त चित्त और किसीका नहीं है; अत: मेरा विचार है कि आप हमारे गुरुजी हो आकर उपस्थित हुए हैं!
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4542)
- **Original**: 18 । ऋशभु बोले-- दे निदाघ ! पहले तुमने सेला-शुअआूषा करके मेथ बहुत आदर किया था अतः तुम्हारे स्लेहवड़ा मैं ऋभु नामक तुम्हारा गुरु हो तमको उपदेश टेनेके त्ख्यि आया हूँ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4543)
- **Original**: हे महामते ! “समस्त पदाधॉमें अद्वैत-आत्म-बुद्धि रखना यही परमार्थका सार है जो मैंने तुम्हें संक्षेपमें उपदेश कर दिया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4544)
- **Original**: ब्राह्मण बोले--निदाघसे ऐसा कह परम विद्वान्‌ गुरूवर भगवान्‌ क्रभु चछ्ते गये और उनके उपदेशसे निदाघ भो अड्वैत-चिच्तनमें तत्पर हो गया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4545)
- **Original**: और सपस्त प्राणियोंकों अपनेसे अभिन्न देखने लगा हे धर्मज़ ! हें पृथिवीपते ! जिस प्रकार उस ब्रह्मपणयण ब्राह्मगने परम मोक्षपद प्राप्त किया, उसी प्रकार तू भी आत्मा, दात्रु और मित्रादिसमें समान भाव रखकर अपनेको सर्वगत जानता हुआ मुक्ति लाभ कर
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4546)
- **Original**: जिस प्रकार एक ही आकाश श्रेत-नील आदि भेदोवाल्म दिखायी देता है, उसी प्रकार भान्तदृष्टियोकों एक ही आत्मा पृथक्‌-पृथक टीखता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4547)
- **Original**: इस संसारमें जो कुछ है वह सब्र एक आत्मा ही है और वर अखिनाशी है, उससे अतिरिक्त और कुछ भी नहीं है; मैं, तू और ये सब आत्मस्वरूप हो हैं। अतः शभेद-ज्ञानरूप मोहकों छोड़ । 23
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4548)
- **Original**: श्रीपराश्रजी बोले--उनके ऐसा कहनेपर सौवीरणजने परमार्थदृष्टिका आश्रय लेकर भेद-बुद्धिको छोड़ दिया और वे जातिस्मर ब्राह्मणग्रेष्ठ. भी बोधयुक्त होनेसे उसी जन्पपें मुक्त हो गये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4549)
- **Original**: इस प्रकार
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4550)
- **Original**: महाराज भरतके इतिहासके इस सारभूत वुत्तान्तको जो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4551)
- **Original**: पुरुष भक्तिपूर्व कहता या सुगता है उसकी युद्धि निर्मल हो जातो है, उसे कभी आत्म-विस्मृति नहों होती और वह जन्म-जन्मात्तरमें मुक्तिकी योग्यता प्राप्त कर भवति चर संसरणेषु मुक्तियोग्य:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4552)
- **Original**: छेता है 25
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4553)
- **Original**: इति श्रीविष्णुपुराणे द्वितीयें$शे पोडशो5घ्याय:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4554)
- **Original**: डति श्रीपराशरसुनिविरचिते श्रीविष्णुपरत्वनिर्णांयके श्रीमति विष्णुमहापुराणे द्वितीयोंडश: समाप्त:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4555)
- **Original**: खनन जै “ना
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4556)
- **Original**: ड्ऊँ श्रीमज्लारायणाय नमः श्रीविष्णुपुराण पहला अध्याय पहले सात मन्वन्तरॉके मनु, इन्द्र, देखता, सप्तर्षि और मनुपुन्रोंका बर्णन औ्रमैत्रेय उवाच कथिता गुरुणा सम्यग्भूसम्रुद्रादिसंस्थिति: । सूर्यादीनां च॒ संस्थान ज्योतिषां चातिविस्तरात्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4557)
- **Original**: 1 देवादीनां तथा सृष्टिऋरषीणां चापि वर्णिता । चातुर्व््यस्य चोत्पत्तिस्तियग्योनिगतस्थ च
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4558)
- **Original**: 2 ध्रुवप्रह्मादचरित बिस्तराध्त्वयोदितम। मन्वन्तराण्यशेषाणि श्रोतुमिच्छाम्यनुक्रमात्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4559)
- **Original**: 3 मन्वन्तराधिपांश्षेव.. झक्रदेबपुरोगमान्‌ । भबता कथितानेताड्छलेतुमिच्छाम्यह गुरो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4560)
- **Original**: 4 शपराशर उवाच अतीतानागतानीह यानि मन्वन्तराणि वै। तान्‍्यहं भवत: सम्यक्तथयामि यथाक्रमम्‌
- **Translation**: 

---

