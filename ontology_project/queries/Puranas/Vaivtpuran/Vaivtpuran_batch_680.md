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

### Verse 1 (Vaivtpuran 88.18042)
- **Original**: कृपां कुरु महामाये मम्त शत्रुक्षयं कुरु। इति श्ीब्रह्मवैवर्ते शिवकुतं दुर्गास्तोत्न सम्पूर्णम्‌। (श्रीकृष्णजन्मखण्ड 88। 15-35) 60 क्र 2 22,50050 प्रकृतेर्बनह्याण्डमोहनकवचम्‌ नारद उवाच सर्वज्ञानविशारद । ब्रह्माण्डमोहन॑ नाम प्रकृते: कवच॑ बद
- **Translation**: 

---

### Verse 2 (Vaivtpuran 88.18043)
- **Original**: नारायण उवाच श्रृणु वक्ष्यामि हे वत्स कवचं चर सुदुर्लभम्‌ । श्रीकृष्णनेव कथितं॑ कृपया ब्रह्मणे पुरा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 88.18044)
- **Original**: ब्रह्मणा कथितं सर्व धर्माय जाह्बीतटे । धर्मेण दत्त महां चर कृपया पुष्करे प्रभु:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 88.18045)
- **Original**: ज़िपुरारिश्न॒ यद्‌ धृत्वा जघान त़्िपुरं पुरा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 88.18046)
- **Original**: मुमोच ब्रह्मा यद्‌ धृत्वा मधुकैटभयोर्भयम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 88.18047)
- **Original**: संजहार रक्तबीज॑ यद्‌ थृत्वा भद्रकालिका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 88.18048)
- **Original**: यद्‌ धृत्वा तु महेन्द्रश्न सम्प्राप कमलालयाम्‌ । यद्‌ धृत्वा च महाकालश्षिरजीबी च॒ धार्मिक:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 88.18049)
- **Original**: यद्‌ धृत्वा च महाज्ञानी नन्‍्दी सानन्दपूर्वकम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 88.18050)
- **Original**: यद्‌ धृत्वा च महायोद्धा रामः शत्रुभयंकर:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 88.18051)
- **Original**: यद्‌ धृत्वा शिवतुल्यश्न दुर्वासा ज्ञानिनां वर: । 3» दुर्गेति चतुर्श्यन्त॑ स्वाहान्तो मे शिरोउ5बतु
- **Translation**: 

---

### Verse 11 (Vaivtpuran 88.18052)
- **Original**: भगवन्‌ सर्वर्थर्मन्ञ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 92.19290)
- **Original**: &38 « संक्षिप्त ग्रह्मवैयर्तपुराण « $%$%%5%%%%% # 5 8 # ######## ##################&##%## # ####ऋ## # #% # ## ####ऋ## # ## ##%## # #### # # # चेतन॑ कुरू कल्याणि देहि मामुत्तरं सति । इत्युक्वा चोद्धबस्तत्र प्रणनाम पुनः पुनः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 92.19291)
- **Original**: इत्युद्धवकृत॑ स्तोत्र यः: पठेद्‌ भक्तिपूर्वकम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 92.19292)
- **Original**: इह लोके सुख धुक्‍त्वा यात्यन्ते हरिमन्दिरम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 92.19293)
- **Original**: न भवेद्‌ बन्धुविच्छेदो रोग: शोकः सुदारुणः । प्रोषिता स्त्री लभेत्‌ कान्तं भार्याभेदी लभेत्‌ प्रियाम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 92.19294)
- **Original**: अपुत्रों लभते पुत्रान्‌ निर्धनो लभते धनम्‌ । निर्भूमिर्लभते भूमिं प्रजाहीनो लभेत्‌ प्रजाम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 92.19295)
- **Original**: रोगाद विमुच्यते रोगी बद्धों मुच्येत बन्धनात्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 92.19296)
- **Original**: भयान्मुच्येत भीतस्तु मुच्येतापन्न आपद:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 92.19297)
- **Original**: अस्पष्टकीर्ति: सुयशा मूर्खो भवति पण्डित:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 92.19298)
- **Original**: इति श्रीब्रह्मवैवर्तें उद्धवकृत श्रीराधास्तोत्र सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 92 । 63--93) 83820 स्यकक9000000 उद्धवकृता श्रीराधाप्रार्थना उद्धव उवाच चेतनं॑ कुरू कल्याणि जगन्मातर्नमोउस्तु ते
- **Translation**: 

---

