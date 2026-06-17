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

### Verse 1 (Vaivtpuran 12.6414)
- **Original**: चरणकमलका स्पर्श कराते हुए कहा-'गज! तू तथा कैलासवासी जन यह दृश्य देखकर आश्चर्यचकित
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6415)
- **Original**: अपने कुदुम्बके साथ एक कल्पपर्यन्त जीवित हो गये। उस समय उनकीौ दशा चित्रलिखित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6416)
- **Original**: रह।' यों कहकर मनके समान वेगशाली भगवान्‌ पुत्तलिकाके समान जड़ हो गयी। कैलासपर आ पहुँचे। वहाँ पार्वतीके वासस्थानपर इस प्रकार उन सबको मूर्च्छित देखकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6417)
- **Original**: आकर उन्होंने उस बालककों अपनी छातीसे श्रीहरि गरुड़पर सवार हुए और उत्तरदिशामें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6418)
- **Original**: चिपटा लिया और उस हाथीके मस्तकको सुन्दर स्थित पुष्पभद्राके निकट गये। वहाँ पुष्पभद्रा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6419)
- **Original**: बनाकर बालकके धड़से जोड़ दिया। फिर नदीके तटपर बनमें स्थित एक गजेन्द्रको देखा,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6420)
- **Original**: ब्रह्मस्वरूप भगवानने ब्रह्मज्ञानसे हुंकारोच्चारण जो निद्राके वशीभूत हो बच्चोंस घिर्कर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6421)
- **Original**: किया और खेल-खेलमें ही उसे जीवित कर हथिनीके साथ सो रहा था। उसका सिर उत्तर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6422)
- **Original**: दिया। पुनः श्रीकृष्णने पार्ववीकों सचेत करके दिशाकी ओर था, मन परमानन्दसे पूर्ण था और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6423)
- **Original**: उस शिशुको उनकी गोदमें रख दिया और बह सुरतके परिश्रमसे थका हुआ था। फिर तो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6424)
- **Original**: आध्यात्मिक ज्ञानद्वारा पार्वतीकों समझाना श्रीहरिने शीघ्र ही सुदर्शनचक्रसे उसका सिर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6425)
- **Original**: आरम्भ किया। काट लिया और रक्तसे भीगे हुए उस मनोहर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6426)
- **Original**: बिष्णुने कहा--शिवे! तुम तो जगत्‌की मस्तककों बड़े हर्षके साथ गरुड़पर रख लिया।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6427)
- **Original**: बुद्धिस्वरूपा हो। क्या तुम नहीं जानतीं कि ब्रह्मासे गजके कटे हुए अज्गजके गिरनेसे हथिनीकी नींद
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6428)
- **Original**: लेकर कीटपर्यन्त सारा जगत्‌ अपने कर्मानुसार टूट गबी। तब अमड्जल शब्द करती हुई उसने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6429)
- **Original**: फल भोगता है। प्राणियोंका जो स्वकर्मार्जित भोग अपने शावकॉंकों भी जगाया। फिर वह शोकसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6430)
- **Original**: है, वह सौ करोड़ कल्पोतक प्रत्येक योनिमें शुभ- विहल हों शावकोंके साथ बिलख-बिलखकर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6431)
- **Original**: अशुभ फलरूपसे नित्य प्राप्त होता रहता है। सती ! चीत्कार करने लगी। तत्पश्चात्‌ जो लक्ष्मीके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.6432)
- **Original**: इन्द्र अपने कर्मवश कीड़ेकी योनिमें जन्म ले स्वामी हैं, जिनका स्वरूप परम शान्त है; जिनके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.6433)
- **Original**: सकते हैं और कीड़ा पूर्वकर्मफलानुसार इन्द्र भी करकमलोंमें श्भु, चक्र, गदा और पद्म शोभा
- **Translation**: 

---

