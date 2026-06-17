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

### Verse 1 (Vishnu Puran 0.10121)
- **Original**: 2 कृतसंवन्दा तेन यथाबइलकेशवोौ । तत:ः प्रविष्टो संहष्टो तमादायात्ममन्दिरम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10122)
- **Original**: हे सह ताभ्यां तदाक्रूरः कृतसंवन्दनादिक: । भुक्तभोज्यो यथान्यायमाचचक्षे ततस्तयो:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10123)
- **Original**: 4 यथा निर्भतिसितस्तेन कंसेनानकदुन्दुभि: । यथा ऋअ देवकी देबी दानवेन दुरात्मना
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10124)
- **Original**: 5 उम्रसेने यथा कंसस्स दुरात्मा च॒ वर्तते। य॑ चैवार्थ समुद्दिश्य कंसेन तु विसर्जित:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10125)
- **Original**: 6 तत्सर्व भगवान्देबकीसुतः । उबाचाखिलमप्येतज्ज्ञात॑ दानपते मया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10126)
- **Original**: 7 करिष्ये तन्यहाभाग यव्त्रौपयिक॑ मतम्‌। विचिन्त्य॑ नान्यथैतत्ते विद्धि कंस हत॑ मया ।। 8 अहं रामश्न मथुरां श्वो यास्यावस्सह त्वया । गोपवृद्धाश्व॒ यास्यन्ति ह्वादायोपायन बहु
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10127)
- **Original**: 9 निशेयं नीयतां वीर न चिन्तां कर्त्तुमहसि । ब्रिरात्राभ्यन्तरे कंसं निहनिष्यासि सानुगम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10128)
- **Original**: 10 श्रीपराहर उयाच समादिद्दय ततो गोपानक़ूरोषपि च केशव: । सुप्राप बलभद्रश्न॒ नन्दगोपगृहे ततः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10129)
- **Original**: 11 ततः प्रभाते बिमले कृष्णरामों महाद्युती
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10130)
- **Original**: अक्ररेण सम गन्तुमुद्यतो मथुरां पुरीम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10131)
- **Original**: 12 दृष्टा गोपीजनस्सास्र: इलथद्डलयबाहुक: । निःशश्वासातिदुःखार््त: प्राह चेदं परस्परम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10132)
- **Original**: 13 मथुरा प्राप्य गोविन्द: कर्थ गोकुलमेष्यति । नगरखसत्रीकलालापमधु श्रोत्रेण पास्यति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10133)
- **Original**: 14 श्रीपराशस्जी जोले--हे मैत्रेय ! यदुवंशी अक्रूरजीने इस प्रकार चिन्तन करते श्रीगोविन्दके पास पहुँचकर उनके चरणोंमें सिर झुकाते हुए 'गैं अक्ल्र हूँ" ऐसा कहकर फ्रणाम किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10134)
- **Original**: 'भगवानने भी अपने ध्वजा- यज-पद्माद्धित करकमलॉसे उल्हें स्पर्शकर और प्रीतिपूर्वक अपनो ओर खींचकऋर गाड़ आलिक्गनन किया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10135)
- **Original**: तदनन्तर अक्रूरजोके यथायोम्य प्रणामादि कर चुकनेपर श्रीबलरामजी और कष्णचन्द्र अति आनन्दित हो उन्हें साथ छेकर अपने घर आये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10136)
- **Original**: फिर उनके द्वारा सत्कृत होकर यथायोग्य भोजनादि कर चुकनेपर अक्कूरने उनसे बह सम्पूर्ण वृत्तान्‍्त कहना आरम्भ किया जैसे कि दुरात्मा दानव कंसने आनकदुन्दुर्भि नसुदेव और टेवो देवक़रोको डाटा था तथा जिस प्रकार वह दुरात्मा अपने पिता उम्सेनसे दुर्व्यवहार कर रहा है और जिस लिये उसने उन्हें (अक्रूरजीको) वृन्दावन भेजा है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10137)
- **Original**: भगवान्‌ देवकौनन्दनने यह सम्पूर्ण कृत्तान्त खिस्तार- पूर्वक सुनकर कहा--“'हे दानपते ! ये सब बातें मुझे मालूम हो गयीं ।
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10138)
- **Original**: है महाभाग ! इस बिषयमें मुझे जो उपयुक्त जान पड़ेगा वही करूँगा। अथ तुम कंसको मेरेद्वारा मरा हुआ ही समझो, इसमें किसी और तरहका लिचार न करो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10139)
- **Original**: भैया बलराम और मैं दोनों ही कल सुम्होरे साथ मथुरा चलेंगे, हमारे साथ ही दूसरे बड़े-बूढे गोप भी बहुत-सा ठपहार छेकर जायैंगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10140)
- **Original**: हे वीर ! आप यह रात्रि सुखपूर्तक बिताइये, किसी प्रकारकी चिन्ता न कीजिये। तीन रात्रिकि भीतर में केसकों उनके अनुचरोंसहित अयश्ष्य मार डालूँगा”
- **Translation**: 

---

