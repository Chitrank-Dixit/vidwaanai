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

### Verse 1 (Vishnu Puran 0.961)
- **Original**: 89 अ्रीविष्णुपुराण [अआ0 9 देवताओंके
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.962)
- **Original**: खोये हुए ] तेजको फिर बढ़ाइये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.963)
- **Original**: श्रीपरादारजी खोले--जिनीत देवताओंदड्राग इस प्रकार स्तुति किये जानेपर विध्वकर्ता भगवान्‌ हरि प्रसन्न होकर इस प्रकार कोले---
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.964)
- **Original**: हे देवगण ! मैं तुम्हारे तेजक्परे फिर बढ़ाऊँगा; तुम इस समय मैं जो कुछ कहता हूँ. वह करो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.965)
- **Original**: तुम दैत्योंकि साथ सम्पूर्ण ओषधियाँ लाकर अमृतके लिये क्षीर-सागरमें डालो और मन्दराचलको मथानी तथा वासुकि नागको नेंती बनाकर उसे दैत्य और दानवोंके सहित मेरी सहायतासे मधकर अमृत निकालो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.966)
- **Original**: तुमस्भेग सामनीतिका अवल्म्नन कर दैत्योंसे कहो कि 'इस काममें सहायता करनेसे आपल्मेग भी इसके फलमें समान भाग पायेंगे'
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.967)
- **Original**: समुद्रके मथनेपर उससे जो अमृत निकलेगा उसका पान करनेसे तुम सबल और अमर हो जाओगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.968)
- **Original**: हे देवगण ! तुम्हारे लिये मैं ऐसी युक्ति करूँगा जिससे तुम्हारे द्वेषी दैत्यॉको अमृत न मिल सकेगा और उनके हिस्सेमें केवल समुद्र-मन्थनका क्रेंशा ही आयेगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.969)
- **Original**: श्रीपराझरजी बोले--तन देवदेव : भगवान्‌ विष्णुके ऐसा कहनेपर सभी देवगण टैस्योंसे सन्धि करके अमृतप्राप्तिक लिये यत्र करने लगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.970)
- **Original**: हे मैत्रेय / देव, दानव और दैत्योंने नाना भ्रकारको ओषधियाँ लाकर उन्हें शरद-ऋतुके आकाशकी-सो निर्मल कान्तिवाले क्षीर-सागरके जलमें डात्ज और मन्दराचलको मथानी तथा वासुकि नागको नेती बनाकर बड़े बेगसे अमृत मथना आरम्भ किया।
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.971)
- **Original**: भगवानने जिस ओर यासुकिकी पुँछ थी उस ओर देवताओंको तथा जिस ओर मुख था उधर दैत्योंको नियुक्त किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.972)
- **Original**: महातेजस्वी वासुकिके मुखसे निकलते हुए निःश्वासाम्रिसे झुलसकर सभी दैत्यगण निस्तेज हो गये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.973)
- **Original**: और उसी श्रास-यायुसे विक्षिप्त हुए सेघोंके पैँछक्ी ओर बरसते रहनेसे देवताओंकी दक्ति बढ़ती गयी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.974)
- **Original**: है महामुने ! भगवान्‌ स्वयं कूर्मरूप घारण कर क्षीर- सागरमें घूमते हुए मन्दराचलके आधार हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.975)
- **Original**: और ये हो चक्र-गदाधर भगवान्‌ अपने एक अन्य रूपसे देवताओमें और एक रूपसे दैत्योंमें मिलकर नागराजको
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.976)
- **Original**: तेजसा नागराजानं तथाप्यायितवान्हरि: । अन्येन तेजसा देवानुपबृंहितवाग्रभुः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.977)
- **Original**: मध्यमाने ततस्तस्मिन्क्षीराब्धौ देवदानवै: । इविर्धामा5भवत्पूव सुरभि: सुरपूजिता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.978)
- **Original**: जम्मुर्मुद॑ ततो देवा दानवाश्च महामुने । व्याक्षिप्रचेतसश्चैव बभूवु: स्तिपितेक्षणा:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.979)
- **Original**: 93 किमेतदिति सिद्धानां दिविचिन्तयतां तत: । बभूव वारुणी देवी मदाधूर्णितलोचना
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.980)
- **Original**: 94 कृताबर्तात्ततस्तस्मान्क्षीरोदाद्नसयद्भगत्‌ । गन्धेन पारिजातो5भूद्देवस्त्रीनन्दनस्तरु:
- **Translation**: 

---

