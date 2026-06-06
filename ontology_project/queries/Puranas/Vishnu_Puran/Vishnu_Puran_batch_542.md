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

### Verse 1 (Vishnu Puran 0.10821)
- **Original**: 7 । --++ # --- इति श्रीतिष्णुपुराणे पश्षमेंडशें पड़लिशोउध्यायः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10822)
- **Original**: न कै -नन+
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10823)
- **Original**: आ0 27 ] पञ्ञम अंश 381 सत्ताईसवाँ अध्याय अद्युज्न-हरण तथा द्ञाम्बर-वध्य आमैत्रेय उवाच झम्बरेण हतो जीरः प्रद्मुज्न:ः स कर्थ मुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10824)
- **Original**: शम्बर: स महावीर्य: प्रद्मु्नेन कर्थ हतः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10825)
- **Original**: 9 यस्तेनापद्दतः पूर्व स कर्थ विजघान तम्‌। एतद्विस्तत: श्रोतुमिच्छामि सकल गुरो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10826)
- **Original**: 2 घष्ठेडह्लि जातमात्रं तु प्रद्युप्न॑ सूतिकागृहात्‌ । हन्तेति मुने हतवान्कालझाम्बर:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10827)
- **Original**: 3 हत्वा चिक्षेप चैबैनं ग्राहोग्रे लूवणार्णवे । कल्लोलजनिताबर्त्ते सुघोरे मकरालये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10828)
- **Original**: 4 पातित॑ तत्र चैबैको मत्स्यों जग्राह बालकम्‌ । न ममार अर तस्थाषि जठराभिप्रदीपितः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10829)
- **Original**: 5 मत्स्यकधैश्र मत्स्यो सौ मत्स्यैरन्यैस्सह द्विज । घातितो5सुरवर्याय शम्बराय निवेदित:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10830)
- **Original**: 6 तस्य मायावती नामपत्नी सर्वगृहेश्वरी । कारयामास सूदानामाधिपत्थमनिन्दिता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10831)
- **Original**: 7 दारिते मत्स्यजठरे सा दरदर्शातिशोभनम्‌। कुमारं मन्मथतरोद्दग्धस्य॒प्रथमाड्ुरप्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10832)
- **Original**: 8 को5उयं कथमयं मत्स्यजटरे प्रविबेशितः । इत्येब॑ कौतुकाविष्टों तन्‍्वीं प्राह्यथ नारदः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10833)
- **Original**: 9 अय॑ समस्तजगतः स्थितिसंहारकारिण: । झाम्बरेण हतो विष्णोस्तनय: सृतिकागृहात्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10834)
- **Original**: 10 क्षिप्तस्समुद्रे मत्स्येन निगीर्णस्ते गृहं गतः । नरस्त्रमिदं सुभ्चु॒ विस्रव्धा परिपालय
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10835)
- **Original**: 11 श्रीपएराशर उवाच नारदेनैबमुक्ता सा पालयामास त॑ शिशुम्‌। बाल्यादेवातिरागेण. रूपातिशयमोहिता
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10836)
- **Original**: 12 स॒यदा योौबनाभोगभूषितो5भून्महामते । साभिलाषा तदा सापि बभूव गजगामिनी
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10837)
- **Original**: 13 श्रीपैत्रेवजोी बोले--हे मुने ! वीरवर प्रध्ुन्नको झम्बरासुरने कैसे हरण किया था? और फिर उस महाबली शम्बरको प्रश्युश्नने कैसे मारा 2
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10838)
- **Original**: जिसको पहले उसने हरण किया था उसीने पीछे उसे किस प्रकार मार डाला ? हे गुगे ! मैं यह सम्पूर्ण प्रसंग विस्तारपूर्वक सुनना चाहता हूँ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10839)
- **Original**: श्रीपराशरजी खोलले--हे मुते ! कालके समान बिकराल हम्बरासुरने प्रधुप्रको, जन्म लेनेके छठे हो दिन 'यह मेरा मारनेवाल्ा है” ऐसा जानकर सूतिकागृहसे हर लिया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10840)
- **Original**: उसको हरण करके शम्बरासुरने लबणसमुद्रमें डाल दिया, जो तरंगमालाजनित आवर्तोंसे पूर्ण और बड़े भयानक मकरोंका घर है
- **Translation**: 

---

