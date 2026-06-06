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

### Verse 1 (Vishnu Puran 0.721)
- **Original**: 2 रुरोद सुस्वर॑ सो5थ प्राद्रवद्द्विजसत्तम । कि त्व॑ रोदिधि ते ब्रह्मा रुदन्तं प्रत्युताच ह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.722)
- **Original**: 3 नाम देहीति त॑ सो5थ प्रत्युवाच्र प्रजापति: । रुत्रस्त्वे देव नाप्लासि मा रोदीर्थैर्ममावह । एबपुक्त: पुनः सो5थ सप्नकृत्वो रुगोद वे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.723)
- **Original**: श्रीपराज्षरजी खोले--हे महामुने !- मैंने तुमसे ब्रह्माजीके तामस-सर्गका वर्णन किया, अब मैं रुद्र- सर्गका वर्णन करता हूँ , सो सुनो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.724)
- **Original**: कल्पके आदियें अपने समान पुत्र उत्पन्न होनेके लिये चिन्तन करते हुए ब्रतह्याजीकी गोदमें नीलछोहित वर्णके एक कुमारका प्रादरर्भाव हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.725)
- **Original**: है है द्विजोत्तम ! जन्मके अन्तर ही वह जोर जोरसे रोने और इचर-उधर दौड़ने छगा। उसे रोता देख ब्रह्माजीनि उससे पूछा--''तू क्‍यों रोता है?”
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.726)
- **Original**: उसमें कहा--“मेरा नाम रखो ।” तथ ब्ह्यांजी बोले--' हे देव ! तेरा नाम रुद्र है,अब तू मतः-रो, 4
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.727)
- **Original**: घैर्य धारण कर।' ऐसा कहनेपर भो वह सात,बार और
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.728)
- **Original**: आअब्8 ] ततोउन्यानि ददौ तस्मै सप्त नाघानि वै प्रभु: । स्थानानि चैषामष्टानां पत्नी: पुत्रांश्न स प्रभु;
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.729)
- **Original**: 5 भय झर्वमथेशान॑ तथा पशुपति द्विज । भीममुर्म॑ महादेवमुबाच॒ स॒पितामह:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.730)
- **Original**: 6 अक्रे नामान्यथैतानि स्थानान्येषां चकार सः । सूर्यो जले मही वादुर्वद्धाराकाशमेण च। दीक्षितो ब्राह्मण: सोम इत्येतास्तनव: क्रमात्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.731)
- **Original**: 7 सुवर्चला तथैयोषा विकेशी चापरा शिवा । स्वाहा दिशस्तथा दीक्षा रोहिणी च यथाक्रपम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.732)
- **Original**: । 8 सूर्यादीनां द्विजश्रेष्त रुद्ाद्ये्नामभिः सह। पल्य: स्मृता महाभाग तदपत्यानि में श्रूणु
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.733)
- **Original**: 9 एषां सूतिप्रसूतिध्यामिदमापूरितं जगत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.734)
- **Original**: 10 झनैश्वरस्तथा भुक्रो छोहिताड़ो मनोजवः । स्कन्दः सर्गो3थ सन्‍्तानो बुधआ्ञनुक्रमात्सुता:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.735)
- **Original**: 11 एवंप्रकारो रद्रोउसौ सती भार्यामनिन्दिताम्‌ । उपयेमे दुहितरं॑ दक्षस्पैवप्रजापते:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.736)
- **Original**: 12 दक्षकोपाच तत्याज सा सती स्वकलेबरम्‌। हिमवददुहिता सा5भून्मेनायां द्विजसत्तम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.737)
- **Original**: 13 उपयेमे पुनश्लोमासनन्यां भगवानहर:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.738)
- **Original**: 14 देवौ धातृविधातारो भृगो: ख्यातिरसूयत । प्रियं च देवदेवस्थ पत्नी नारायणस्य या
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.739)
- **Original**: 157 अऔमैत्रेय उवाच क्षीराब्धौ श्री: समुत्यत्ना श्रूयतेअ्यृतमन्थने । भृगो: ख्यात्यां समुत्यन्नेत्येतदाह कर्थ भवान्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.740)
- **Original**: 16 आपयदार उवाब नित्यैवैषा जगन्माता विष्णो: श्रीरनपायिनी । यथा सर्वगतो बिष्णुस्तथैल्रेय द्विजोत्तम
- **Translation**: 

---

