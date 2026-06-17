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

### Verse 1 (Vishnu Puran 0.9061)
- **Original**: हे द्विज ! अर्द्धरात्रिकि समय सर्वाधार भगवान्‌ जनार्दनके आविर्भूत होनेपर पुष्पठषां करते हुए मेघगण मन्द-मन्द गर्जना करने छगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9062)
- **Original**: उन्हें खिले हुए कमलदलकी-सौ आभावाले, चतुर्भुज ओर बक्षःस्थलमें श्रीबत्स चिद्डसहित उत्पन्न हुए देख आनकरुन्दुभि यसुदेयजी स्वुति करने छगे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9063)
- **Original**: हे द्विजोत्तम ! महामति वसुदेवजीने प्रसादयुक्त बचनोंसे भगवानऊकी स्तुति कर कंससे भयभीत रहनेके कारण इस प्रकार निवेदन किया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9064)
- **Original**: वसुदेवजी बोले--हे देवदेवेश्वर
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9065)
- **Original**: ! यद्यपि आप [ साक्षात्‌ परमेश्वर ] प्रकट हुए हैं, तथापि हे देख ! मुझपर कृपा करके अब अपने इस शक्-चक्र- गदाघारों दिव्य रूपका उपसंहार कीजिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9066)
- **Original**: है देव! यह पता लगते ही कि आप मेंरे इस गृहमें अपतीर्ण हुए हैं, केस इमी समय मेण सर्वनाश कर देगा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9067)
- **Original**: देबकीजी बोलीं--जो अनन्तरूप और अखिल- विश्वस्वरूप हैं, जो गर्भमें स्थित होकर भो अपने शरीरसे सम्पूर्ण ल्लेकॉक्ग्रें धारण करते हैं तथा जिल्‍्होंने अपनी मायासे ही बालरूप धारण किया है वे देवदेव हमपर प्रसन्न हों
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9068)
- **Original**: हे सर्नात्मम्‌ ! आप अपने इस चतुर्भुज़ रूपका उपसंहार कीजिये। भगवन्‌ ! यह राक्षसके अंशसे उत्पन्न" केस आपके इस अबठरका बृत्तात्त न जानने पाबे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9069)
- **Original**: श्रीभगवान्‌ बोले--हे देवि ! पूर्व-जन्ममें सुने लिये ] प्रार्था की थी। आज मैंने तेरे गर्भसे जन्म लिया है--इससे तेरी बह कामना पूर्ण हो गयी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9070)
- **Original**: श्रीपराहशरजी खोल्े--हे सुनिश्नेष् ! ऐसा कहकर भगवान्‌ मौन हो गये तथा वसुदेवजी भी उन्हें उस रात्रिमें हो छेकर बारर निकले
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9071)
- **Original**: यसुदेक्जीके बाहर जाते समय क्राणगृतरक्षक और मथुराक्रे द्वारपारू योगनिद्राके # द्रुमिक्नामक राक्षसने राजा उग्सेगका रूप धारण कर उनकी पत्नीसे संसर्ग किया था । उसीसे कैसका जन्म हुआ। यह कथा हरिसेद्ामें आयी है।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9072)
- **Original**: आ $ ] वर्षतां जलदानां च तोयमत्युल्बर्ण निशि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9073)
- **Original**: संवृत्यानुययां शेष: फणैरानकदुन्दुभिम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9074)
- **Original**: 17 यपुनां चातिगम्भीरां नानावर्त्तशताकुछाम। वसुदेवो वहन्विष्णुं जानुमात्रवहां ययो
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9075)
- **Original**: 18 कंसस्थ करदानाय तज्नैवाभ्यागतांस्तटे । नन्दादीन्‌ गोपवृद्धांश् यमुनाया ददर्श सः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9076)
- **Original**: 19 तस्मिन्काले यशोदापि मोहिता योगनिद्रया । तामेव कन्या मैत्रेय प्रसूता मोहते जने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9077)
- **Original**: 20 वसुदेवो5पि विन्यस्य वालमादाय दारिकाम्‌ । यशोदाइयनात्तूर्णमाजगामामितझयुति:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9078)
- **Original**: 21 ददूशे च प्रबुद्धा सा यश्लोदा जातमात्मजम्‌ । नीलछोत्पलदलइ्यामं ततोउत्यर्थ मुदं ययौ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9079)
- **Original**: 22 आदाय यसुदेयो5पि दास्किं निजमन्दिरे। देवकीशायने न्‍्यस्थ यथापूर्वमतिष्ठत
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9080)
- **Original**: 23 ततो बालथ्वर्नि भ्रुत्वा रक्षिणस्सहसोत्थिता: । कंसायाबेदयामासुर्देबकीप्रसत द्विज
- **Translation**: 

---

