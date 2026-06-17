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

### Verse 1 (Rig Ved 0.10361)
- **Original**: 4503. अग्न आ याहि बीतये गृणानो हव्यदातये । नि होता सत्सि बर्हिषि
- **Translation**: 

---

### Verse 2 (Rig Ved 0.10362)
- **Original**: है अम्निदेव ! हे प्रकाशक एवं सर्वव्यापक देव ! हवि को गति देने (वीति) के लिए आप पधारें। सब आपकी स्तुति करते हैं । यज्ञ में हम आपका आवाहन करते है; क्योंकि आप सब पदार्थों को प्रदान करने वाले हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.10363)
- **Original**: 4504. त॑ त्वा समिद्धिरड्रिरो घृतेन वर्धयामसि । बृहच्छोचा यविष्ठ्य
- **Translation**: 

---

### Verse 4 (Rig Ved 0.10364)
- **Original**: हे प्रकाशस्वरूप परप्ात्मन्‌ ! हम आपको समिधाओं तथा घृत द्वारा प्रदीष्त करते हैं। अत: हे सामर्थ्यवान्‌ ! आप अधिक प्रखर हों
- **Translation**: 

---

### Verse 5 (Rig Ved 0.10365)
- **Original**: 4505, स नः पृथु श्रवाय्यमच्छा देव विवाससि । बृहदम्ने सुवीर्यम्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.10366)
- **Original**: है अग्निदेव ! आप ऐसी कृपा करें कि हम महान्‌ पराक्रम और श्रेष्ठ यशस्वी सामर्थ्य प्राप्त हो
- **Translation**: 

---

### Verse 7 (Rig Ved 0.10367)
- **Original**: मं0 6 सू0 16 21 4506. त्वामग्ने पुष्करादध्यथर्वा निरमन्थत। मूध्नों विश्वस्य वाघत:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.10368)
- **Original**: परम श्रेष्ठ, अखिल विश्व के धारणकर्ता हे अग्निदेव ! अथर्वा (विज्ञानवेत्ता अथवा प्रधान प्रोहित) ने आपको विश्व के महानतम आधार के रूप में अरणि मन्थन द्वारा प्रकट किया
- **Translation**: 

---

### Verse 9 (Rig Ved 0.10369)
- **Original**: 4507 तमु त्वा दघ्यड्डडषि: पुत्र ईथे अथर्वण: । वृत्रहणं पुरन्दरम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.10370)
- **Original**: हे अग्निदेव ! 'अधर्वा' के पुत्र 'दध्यड्‌' ऋषि ने आपको प्रथम प्रदीप्त किया । आप शत्रुसंहारक एवं उनके नगरों को नष्ट करने वाले हैं
- **Translation**: 

---

### Verse 11 (Rig Ved 0.10371)
- **Original**: 4508. तमु त्वा पाथ्यो वृषा समीधे दस्युहन्तमम्‌। धनज्जयं रणेरणे
- **Translation**: 

---

### Verse 12 (Rig Ved 0.10372)
- **Original**: हे अग्निदेव ! “पाथ्य वृषा “(इस नाम के ऋषि अथवा सन्मार्गगामी बलवान) ने आपको प्रदीप्त किया । आप असुर संहारक तथा युद्ध में जीतने वाले हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.10373)
- **Original**: 4509, एह्यू षु ब्रवाणि तेडग्न इत्थेतरा गिर: । एमिव॑र्धास इन्दुभि:
- **Translation**: 

---

### Verse 14 (Rig Ved 0.10374)
- **Original**: हम आपके लिए ही स्तुति करते हैं। आप इन्हें सुनकर प्रकट हों और इस सोमरस से अपनी महानता का विस्तार करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.10375)
- **Original**: 4510. यत्र क्व च ते मनो दक्ष॑ दधस उत्तरम्‌। तत्रा सदः कृणवसे
- **Translation**: 

---

### Verse 16 (Rig Ved 0.10376)
- **Original**: हे अग्निदेव ! आप जिस क्षेत्र एवं याजक से प्रसन्न होते हैं, वहों अधिकाधिक बल धारण कराते हैं और वहीं आवास भी बनाते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.10377)
- **Original**: 4511. नहि ते पूर्तमक्षिपद्धुवन्नेमानां वसो । अथा दुबो बनवसे
- **Translation**: 

---

### Verse 18 (Rig Ved 0.10378)
- **Original**: हे अग्निदेव ! आपका तेज चक्षुओं के लिए हानिकारक नहीं है । हे ब्रपालक मानवों के स्वामी
- **Translation**: 

---

### Verse 19 (Rig Ved 0.10379)
- **Original**: ! आप हमारी प्रार्थना स्वीकार करें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.10380)
- **Original**: [ सापान्य माय्यता यह है कि गर्मी से आँखों को हानि पहुँचती है; किनु यज़ीय ऊर्जा नेत्रों के लिए भी हिलकारी है ।] 4512. आम्निरगामि भारतो वृत्रहा पुरुचेतन: । दिवोदासस्य सत्पति:
- **Translation**: 

---

