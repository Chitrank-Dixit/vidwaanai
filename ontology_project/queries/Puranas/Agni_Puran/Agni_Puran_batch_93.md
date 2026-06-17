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

### Verse 1 (Agni Puran 0.1841)
- **Original**: परम शिवमें योजनिकाकी स्थिरताके लिये “30 नमः शिवाय वौषटू।'--इस मन्त्रका उच्चारण करते हुए अग्निकी ज्वालामें घीकी धारा छोड़ता रहे। फिर विधिपूर्वक पूर्णाहुति देकर गुणापादन करे। उसकी विधि इस प्रकार है। निम्नाद्धित मन्त्रोंको पढ़कर अग्निमें आहुतियाँ दे-- “3» हां आत्मन्‌ सर्वज्ञों भव स्वाहा।' ' 3» हीं आत्मन्‌ नित्यतृप्तो भव स्वाहा।' '3» हूं आत्मन्‌ अनादिबोधो भव स्वाहा।' ' 30 हैं आत्मन्‌ स्वतन्त्रो भव स्वाहा।' “30 हा आत्मन्‌ अलुप्तशक्तिर्भव स्वाहा।' ' 3» ह; आत्मन्‌ अनन्तशक्तिर्भव स्वाहा ।' * अद्गुलविस्तृतस्प ललासस्पोध्य॑प्रदेशों द्रादशान्सपदेनोच्यते।' अर्थात्‌ “अब्रुल बिस्तारबाले ललाटका ऊर्ध्यदेश “ढादशान्त' पदसे कथित होता है।' (“नित्याषोडशिकाएँव” 8
- **Translation**: 

---

### Verse 2 (Agni Puran 0.1842)
- **Original**: 55 पर भास्कररायकौ सेतुबन्ध-ख्याख्या)
- **Translation**: 

---

### Verse 3 (Agni Puran 0.1843)
- **Original**: * अध्याय 90 * 193 इस प्रकार छः गुणोंसे सम्पन्न आत्माको अविनाशी
- **Translation**: 

---

### Verse 4 (Agni Puran 0.1844)
- **Original**: हुए इस जीवको. आपने ही अनुगृहीत किया है परमशिवसे लेकर विधिवत्‌ भावनापूर्वक शिष्यके
- **Translation**: 

---

### Verse 5 (Agni Puran 0.1845)
- **Original**: अत: नाथ! देवता, अग्नि तथा गुरुमें इसकी भक्ति शरीरमें नियोजित करे। तीव्र और मन्द शक्तिपातजनित
- **Translation**: 

---

### Verse 6 (Agni Puran 0.1846)
- **Original**: बढ़ाइये'
- **Translation**: 

---

### Verse 7 (Agni Puran 0.1847)
- **Original**: श्रमकी शान्तिके लिये शिष्यके मस्तकपर न्यासपूर्यक
- **Translation**: 

---

### Verse 8 (Agni Puran 0.1848)
- **Original**: इस प्रकार प्रार्थना करके देवेश्वर शिवको प्रणाम अमृत-बिन्दु अर्पित करें
- **Translation**: 

---

### Verse 9 (Agni Puran 0.1849)
- **Original**: 532--57
- **Translation**: 

---

### Verse 10 (Agni Puran 0.1850)
- **Original**: करनेके अनन्तर गुरु स्वयं शिष्यको आदरपूर्वक यह ईशान-कलश आदिके रूपमें पूजित शिवस्वरूप
- **Translation**: 

---

### Verse 11 (Agni Puran 0.1851)
- **Original**: आशीर्वाद दे कि “तुम्हारा कल्याण हो '। इसके बाद कलशोंको नमस्कार करके दक्षिणमण्डलमें शिष्यको
- **Translation**: 

---

### Verse 12 (Agni Puran 0.1852)
- **Original**: भगवान्‌ शिवकों उत्तम भक्तिभावसे आठ फूल अपने दाहिने उत्तराभिमुख बिठावे और देवेश्वर
- **Translation**: 

---

### Verse 13 (Agni Puran 0.1853)
- **Original**: चढ़ाकर शिवकलशके जलसे शिष्यकों स्नान करवाबे शिवसे प्रार्थना करे--'प्रभो! मेरी मूर्तिमें स्थित
- **Translation**: 

---

### Verse 14 (Agni Puran 0.1854)
- **Original**: और यज्ञका विसर्जन करे
- **Translation**: 

---

### Verse 15 (Agni Puran 0.1855)
- **Original**: इस प्रकार आदि आरनेब महापुराणमें “निर्वाण-दीक्षाका वर्णन” तामक अठासीवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 16 (Agni Puran 0.1856)
- **Original**: / नंवासीयाँ अध्याय एकतत्त्व-दीक्षाकी विधि* भगवान्‌ शिव कहते हैं--स्कन्द! अब लघु
- **Translation**: 

---

### Verse 17 (Agni Puran 0.1857)
- **Original**: संस्कारोंका पूर्ववत्‌ सम्पादन करे; किंतु मूल-मन्त्रसे होनेके कारण एकतात्तविकौ-दीक्षाका उपदेश दिया
- **Translation**: 

---

### Verse 18 (Agni Puran 0.1858)
- **Original**: सर्वशुल्क समर्पण करे। इसके बाद तत्त्वसमूहोंसे जाता है। यधावसर यथोचित रीतिसे स्वकीय
- **Translation**: 

---

### Verse 19 (Agni Puran 0.1859)
- **Original**: गर्भित पूर्णाहुति प्रदान करे। उस एक ही आहुतिसे मन्त्रद्वार सूत्रबन्ध आदि कर्म करे। तत्पश्चात्‌ काल,
- **Translation**: 

---

### Verse 20 (Agni Puran 0.1860)
- **Original**: शिष्य निर्बाण प्राप्त कर लेता है
- **Translation**: 

---

