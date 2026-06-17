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

### Verse 1 (Vishnu Puran 0.5961)
- **Original**: है राजन्‌ ! इस सम्बन्धमें एक गाथा सुनी जाती है जो पूर्वकालमें मनुपुत्र महागज इक्ष्वाकुकते प्रति पित॒गणने कठ्ग्रप उपलनमें कही थो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5962)
- **Original**: “क्या हमारे कुलपें ऐसे सन्मार्ग-झीरू व्यक्ति होंगे जो गयामें जाकर हमारे लिये आदरपूर्वक फिष्डदान करेंगे ?
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5963)
- **Original**: क्‍या हमारे कुलूसें कोई ऐसा पुरुष होगा जो वर्षाकालकी मघानक्षत्रयुक्त त्रयोदशीको हमारे उद्देहयसे मधु और घृतयुक्त पायस (खीर) का दान करेगा ?
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5964)
- **Original**: अ0 157 ] तृतीय अंडा 21575 गौरीं वाप्युद्वेत्कन्यां नील वा वृषमुत्सूजेत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5965)
- **Original**: यजेत वाश्रवमेधेन विधिवद॒क्षिणावता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5966)
- **Original**: 20 अथवा गौरी कन्यासे बिवाह करेगा, नौला वृषभ छोड़ेगा या दक्षिणासहित विधिपूर्वक अश्रमेध यज्ञ करेगा ?'
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5967)
- **Original**: कततत औ तन इति श्रीविष्णुपुराणे तृतीयें5शे पोडशो5ध्याय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5968)
- **Original**: कचत औ क्‍+ सत्रहवाँ अध्याय नपभ्नविषयक प्रश्न, देशताओंका पराजय, उनका भगवान्‌की हरणमें जाना और भगवानका मायामोहको प्रकट करना डत्याह भगवानोौर्वस्सगराय. महात्मने । सदाचार॑ पुरा सम्यडः मैत्रेय परिपृच्छते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5969)
- **Original**: 9 मयाप्येतदशेषेण कथित भवतो द्विज । समुल्लद्घ्य सदाचारं कश्निन्नाप्रोति शो भनम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5970)
- **Original**: 2 श्रीमैतरेय उवाच घण्डापविद्धप्रमुखा विदिता भगवन्‍्पया। उदक्याद्याअ में सम्यह्ट नप्नमिच्छामि वेदितुम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5971)
- **Original**: 3 को नप्नः कि समाचारो नभनसंज्ञां नरो वूभेत्‌ । नभ्नस्वरूपमिच्छामि यथावत्कथितं त्वया। श्रोतुं धर्मभृतां श्रेष्ठ न ह्वास्यविदितं तब
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5972)
- **Original**: 4 श्रीपयाद्ार उबाच एतामुज्झति यो मोहात्स नम्न: पातकी द्विज:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5973)
- **Original**: 5 त्रयी समस्तवर्णानां द्विज संवरण यतः। नझ्नो भवत्युण्झितायामतस्तस्यां न संशय:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5974)
- **Original**: 6 डे च श्रूयतामन्यद्यद्धीष्माय महात्मने । कशथयामास थधर्मज्ञो वसिष्ठोउस्मत्पितामह:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5975)
- **Original**: 7 मयापि तस्थ गदतइसश्लुतमेतन्महात्मनः । नग्नसम्बन्धि मैत्रेय यत्पृष्टोहहमिह त्वया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5976)
- **Original**: 8 देवासुरमभूझुद्ध दिव्यमब्दहात॑ पुरा । तस्मिन्पराजिता देवा दैत्यैल्लांदपुरोगमै:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5977)
- **Original**: 9 क्षीरोदस्पोत्तरं कूल गत्यातप्यन्त सै तपः । विष्णोराराधनार्थाय जगुश्चैम॑ स्तव॑ तदा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5978)
- **Original**: 190 श्रीपराशरजी जोल्के--हे मैत्रेय ! पूर्वकालमें महात्मा सगरसे उनके पूछनेपर भगवान्‌ और्वने इस प्रकार गृहस्थके सदाचारका निरूपण किया था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5979)
- **Original**: हे ट्विज ! मैंने भी तुमसे इसका पूर्णतया वर्णन कर दिया। उ््रेई भी पुरुष सदाचारका उल्लक्लुन करके सद्गति नहों फा सकता
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5980)
- **Original**: श्रीमै्रेयजी खोले--भगवन्‌ ! नपुंसक, अपविद्ध और रजस्वलछा आदिको तो मैं अच्छी तरह जानता हैं. [किन्तु यह नहीं जानता कि “नमन” क्रिसको कहते हैं] । अतः इस समय मैं नप्रके विषयमें जानना चाहता हूँ
- **Translation**: 

---

