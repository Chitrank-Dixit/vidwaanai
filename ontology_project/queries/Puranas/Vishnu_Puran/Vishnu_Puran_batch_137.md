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

### Verse 1 (Vishnu Puran 0.2721)
- **Original**: नेवस्वत-मन्वन्तरके आर्म्भमें महान्‌ वारुण यज्ञ हुआ, उसमें ब्रह्माजी होता थे, अब मैं उनकी प्रजाका वर्णन करता हूँ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2722)
- **Original**: हे साधुश्रेष्ठ ! पूर्व-मन्वन्तरमें जो सप्तर्षिगण स्कये ब्रह्माजीके पानसपुत्ररूपसे उत्पन्न हुए थे, उन्हींको बह्याजाने इस कल्पमें गन्धर्व, नाग, देव और दानवादिके पितृरूपसे निश्चित किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2723)
- **Original**: पुत्रोके नष्ट हो जानेपर दितिने कश्यपजीको प्रसन्न किया। उसकी सम्यक्‌ आयधनासे सन्‍्तुष्ट हो तपस्थियोँमें श्रेष्ठ कश्यपजीने उसे वर देकर प्रसन्न किया। उस समय उसने इन्द्रके वध करनेमें समर्थ एक अति तेजस्वी पुत्रका जर माँगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2724)
- **Original**: 94 आआआआश्रीविष्मुपराण आफ जआरर 8 आ्रोविष्णुपुराण [(ऋ 21 सच तस्मै बर॑ प्रादाद्धार्यय मुनिसत्तम: । क्यपजीने अपनी भार्या दितिको बह बर दत््वा च वरमत्युग्रे कश्यपस्तामुवाच ह
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2725)
- **Original**: 32 दिया £: 947 अति उप्र वर्को देते हुए यें उससे बोले--- जञक फुतो ते यदि गर्भ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2726)
- **Original**: “यदि तुम भगवान्‌के ध्यानमें तत्पर रहकर निहन्ता गर्भ शरच्छतम
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2727)
- **Original**: अपना गर्थ ज्ौच* और संयमपूर्वक सौ वर्षतक धारण समाहितातिप्रयता ज्ौचिनी धारयिष्यसि
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2728)
- **Original**: कर सकोगी तो दुम्हारा पुत्र इन्द्रको मारनेवाल्त्र इत्येवपुक्ल्वा तां देवीं सड्त्त: कश्यपो मुनि: । होगा”
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2729)
- **Original**: ऐसा कहकर मुनि कश्यपजोने उस देवीसे दधार सा च त॑ गर्भ सम्यक्छौचसमन्विता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2730)
- **Original**: 34 गर्भमात्मवधार्थाय ज्ञात्वा त॑ मघवानपि। शुश्रूषुस्तामथागच्छट्चिनयादमराधिप:._
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2731)
- **Original**: 35 तस्वाश्ैवान्तरप्रेप्सुरतिप्तत्पाकशासन: ..
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2732)
- **Original**: ऊने बर्षशते चास्था ददशान्तिरमात्मना
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2733)
- **Original**: 36 अकृत्वा पादयो: झौच दितिः शयनमाविशत्‌। निद्रा चाहारयामास तस्या: कुक्षिं प्रविश्य सः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2734)
- **Original**: 37 कज़पाणिर्महागर्भ चिच्छेदाथ स सप्तथा। सम्पीड्यमानों वद्रेण स रुरोदातिदारुणम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2735)
- **Original**: 38 मा रोदीरिति ते शक्रः पुनः पुनरभाषत । सो5भवत्सप्धा गर्भस्तमिन्द्र: कुपित: पुनः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2736)
- **Original**: 39 एकैकं सप्तथा चक्रे क्ज्रेणारिविदारिणा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2737)
- **Original**: मरुतो नाम देवास्ते बभूबुरतिबेगिन:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2738)
- **Original**: 40 यतुक्ते वै भगवता तेनैब मरुतो$भवन्‌। देवा एकोनपश्चाइत्सहाया वज्रपाणिन:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2739)
- **Original**: 49 संगमन किया और उसने बड़े शौचपूर्यक रहते हुए बह गर्भ धारण किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2740)
- **Original**: उस गर्भको अपने वधका कारण जान -देवगज इन्द्र भी विनयपूर्वक उसकी सेवा करनेके लिये आ गये
- **Translation**: 

---

