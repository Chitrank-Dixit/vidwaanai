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

### Verse 1 (Vaivtpuran 7.9593)
- **Original**: तुरंत शिशुरूप हो गये। कश्यप थे और ये सुतपा माता अदिति तुम्हारे श्यामल पुत्रकों पृथ्वीपर नग्रभावसे सोया साथ थीं। तुमने अपनी इन तपस्विनी पत्नी देख विष्णुकी मायासे मोहित हो वसुदेवजी अदितिके साथ तपस्याद्वारा मेरी आराधना की थी।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9594)
- **Original**: सूतिकागारमें अपनी स्त्रीसे तन्द्रामें बोले-प्रिये! वहाँ मुझे देखकर तुमने मेरे समान पुत्र होनेका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9595)
- **Original**: यह कैसा तेजःपुझ्म है?! ऐसा कह वसुदेवने बर माँगा और मैंने भी तुम्हें यह वर दिया कि
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9596)
- **Original**: पत्रेके साथ कुछ विचार करके बालकको गोदमें मेरे समान पुत्रकी प्राप्ति होगी। तात! तुम्हें वर उठा लिया और उसे लेकर बे नन्द-गोकुलमें देकर मैंने मन-ही-मन विचार किया। फिर यह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9597)
- **Original**: जा पहुँचे। वहाँ नन्दगाँवमें यशोदा नींदसे अचेत बात ध्यानमें आयी कि मेरे समान तो कोई
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9598)
- **Original**: हो रही थीं। उन्होंने शय्यापर उन्हें निद्रित त्रिभुवनमें है ही नहीं। इसलिये मैं स्वयं ही तुम्हारे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9599)
- **Original**: अवस्थामें देखा। साथ ही ननन्‍्दजी भी वहाँ नींदमें पुत्रभावको प्राप्त हुआ। आप स्वयं कश्यपजी हैं
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9600)
- **Original**: बेसुध हो रहे थे। वहाँ घरमें जो कोई भी प्राणी और तपस्याके प्रभावसे इस समय मेरे पिता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9601)
- **Original**: थे, सब सो गये थे। बसुदेवजीने देखा, तपाये वसुदेव हुए हैं। ये उत्तम तपस्यावाली पतित्रता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9602)
- **Original**: हुए सुवर्णके समान गौर कान्तिवाली एक नग्र देवमाता अदिति ही इस समय अपने अंशसे मेरी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9603)
- **Original**: बालिका पड़ी-पड़ी घरकी छतकी ओर दृष्टिपात * श्रीमन्तमिन्द्रियातीतमक्षरं निर्गुण विभुम्‌। ध्यानासाध्य॑ च सर्वेषां परमात्मानमी श्वरम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9604)
- **Original**: स्वेच्छामर्य सर्वरूप॑ स्वेच्छारूपधर॑ परम्‌ । निर्लिपं परम॑ ब्रह्म बीजरूप॑ सनातनम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9605)
- **Original**: स्थूलातू स्थूलतरं व्याप्तमतिसूक्ष्ममदर्शमम्‌ । स्थितं. सर्वशरीरिषु. साक्षिरूपमदृश्यकम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9606)
- **Original**: शरीरवन्त॑ सगुणमशरीरं गुणोत्करम्‌ । प्रकृतिं प्रकृतोशं चर प्राकृत॑ प्रकृते: परम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9607)
- **Original**: सर्वेशं सर्वरूप॑ च॒ सर्वान्तकरमव्ययम्‌ । सर्वाधारं निशधार॑ निर्व्यूहं स्तौमि कि विभो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9608)
- **Original**: अनन्त: स्तवने5शक्तो5शक्ता देवी सरस्वती । य॑ स्तोतुमसमर्थश्ष पश्वक्त्र: . षड़ानन:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9609)
- **Original**: चतुर्मुखो वेदकर्ता य॑ स्तोतुमक्षम: सदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9610)
- **Original**: गणेशो न समर्थक्ष योगीद्धाणां गुरोगुरु:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9611)
- **Original**: ऋषयों देवताश्चैव मुतौद्धमनुमानवा: । स्वप्रे तेषामदृश्यं च त्वामेय॑ कि स्तुवन्ति ते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9612)
- **Original**: श्रुतप: स्तवनेठशक्ता: कि स्तुबन्ति विपश्चित:। विहायैवं शरीर॑ च बालो भवितुमरईसि
- **Translation**: 

---

