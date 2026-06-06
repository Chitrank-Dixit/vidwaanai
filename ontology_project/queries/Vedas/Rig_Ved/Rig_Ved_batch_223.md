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

### Verse 1 (Rig Ved 0.4441)
- **Original**: 1969. सुरुक्‍्मे हि सुपेशसाधि श्रिया विराजत:। उषासावेह सीदताम्‌
- **Translation**: 

---

### Verse 2 (Rig Ved 0.4442)
- **Original**: उत्तम स्वरूप वाली (उषा एवं रात्रि) और अधिक शोभा पा रही हैं । है उषा और रात्रि ! आप दोनों हमारे यहाँ यज्ञ में विराजमान हों
- **Translation**: 

---

### Verse 3 (Rig Ved 0.4443)
- **Original**: 1970. प्रथमा हि सुवाचसा होतारा दैव्या कवी। यज्ञ नो यक्षतामिमम्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.4444)
- **Original**: सर्वोत्तम, प्रखर वाणी के प्रयोक्ता, दिव्यगुणों से युक्त मेधावी होता हमारे इस यज्ञ को सम्पन्न करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.4445)
- **Original**: 1971. भारतीछे सरस्वति या व: सर्वा उपब्ुवे। ता नश्चोदयत श्रिये
- **Translation**: 

---

### Verse 6 (Rig Ved 0.4446)
- **Original**: हे भारती, इत्म और सरस्वती ! हम आप सभी को आमंत्रित करते हैं। आप तीनों हमें ऐश्वर्य विभूतियों की ओर प्रेरित करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.4447)
- **Original**: 1972 . त्वष्टा रूपाणि हि प्रभु: पशून्विश्वान्समानजे। तेषां न: स्फातिमा यज
- **Translation**: 

---

### Verse 8 (Rig Ved 0.4448)
- **Original**: त्वष्टादेव स्वरूप प्रदान करने में सक्षम हैं, बहो पशुओं के निर्माता हैं। हे त्वष्टादेव ! आप हमारे लिए पशुधन को बृद्धि करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.4449)
- **Original**: 1973. उप त्मन्या वनस्पते पाथो देवेभ्य: सृज । अर्ग्निहव्यानि सिष्वदत्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.4450)
- **Original**: हे बनस्पते ! आप अपनी सामर्थ्य से हव्य पदार्थ उत्पन्न करें, तब अग्निदेव हव्य का सेवन करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.4451)
- **Original**: 1974. पुरोगा अम्निर्देवानां गायत्रेण समज्यते
- **Translation**: 

---

### Verse 12 (Rig Ved 0.4452)
- **Original**: स्वाहाकृतीषु रोचते
- **Translation**: 

---

### Verse 13 (Rig Ved 0.4453)
- **Original**: देवताओं में अयणी रहनेवाले अग्निदेव गायत्री मंत्र के उच्चारण से सुशोभित होते हैं; पश्चात्‌ “स्वाहा” शब्द के साथ प्रदत्त आहुतियों से वे अग्निदेव प्रज्जलित होते हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.4454)
- **Original**: 286 ऋत्वेद संहिता पाग-9 [ सूक्त - 189 ] ( ऋषि- आगस्त्य मैत्रावरुणि
- **Translation**: 

---

### Verse 15 (Rig Ved 0.4455)
- **Original**: देवता - अग्नि
- **Translation**: 

---

### Verse 16 (Rig Ved 0.4456)
- **Original**: न्द- विष्टप्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.4457)
- **Original**: ] 1975 अग्ने नय सुपथा राये अस्मान्विश्वानि देव वयुनानि विद्वान्‌। युयोध्य9 स्मज्जुहुराणमेनो भूयिष्ठां ते नमउक्ति विधेम
- **Translation**: 

---

### Verse 18 (Rig Ved 0.4458)
- **Original**: दिव्य गुणों से मुक्त है अग्निदेव ! आप सम्पूर्ण मार्गों (ज्ञान) को जानते हुए हम याजकों को यज्ञ फल प्राप्त करने के लिए पर ले चलें । हमें कुटिल टिल आचरण करने वाले जञत्रुओं तथा पापों से मुक्त करें हम आपके लिए स्तोत्र एवं नम्स्कारों का विधान करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.4459)
- **Original**: 1976. अग्ने त्वं पारया नव्यो अस्मान्त्स्वस्तिभिरति दुर्गाणि विश्वा। पृक्ष पृथ्वी बहुला न उर्वी भवा तोकाय तनयाय शं यो:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.4460)
- **Original**: है आत्निदेव !आप नित्यनूतन अथवा अति प्रशंसनीय हैं ।आपकी कृपा से मंगलकारी मार्गों से हम सभी प्रकार के दुर्गम पापकर्मों एवं कष्टकारी दुःखों से निवृत्त हों । बह पृथ्वी और नगर हमारे लिए उत्तम और विस्तृत हों। आप हमारी सन्‍्तानों के लिए सुखप्रदायी हों
- **Translation**: 

---

